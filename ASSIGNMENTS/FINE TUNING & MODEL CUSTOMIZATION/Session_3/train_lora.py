"""Tiny LoRA sentiment fine-tuning example; saves adapter and reports its size."""
from pathlib import Path
import shutil
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from peft import LoraConfig, TaskType, get_peft_model

MODEL="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
texts=["Loved the meal, fresh and delicious", "Fast delivery and tasty food", "Wonderful service", "A perfect dinner",
       "Cold food and very late", "Missing items and no help", "Terrible taste", "The order was disappointing",
       "Great portions and flavor", "The packaging leaked"]
labels=[1,1,1,1,0,0,0,0,1,0]
tok=AutoTokenizer.from_pretrained(MODEL)
ds=Dataset.from_dict({"text":texts,"labels":labels}).map(lambda b:tok(b["text"],truncation=True,padding="max_length",max_length=96),batched=True)
ds=ds.remove_columns(["text"])
model=AutoModelForSequenceClassification.from_pretrained(MODEL)
model=get_peft_model(model,LoraConfig(task_type=TaskType.SEQ_CLS,r=4,lora_alpha=8,lora_dropout=.1,target_modules=["q_lin","v_lin"],modules_to_save=["pre_classifier","classifier"]))
out=Path("lora-food-review-adapter")
args=TrainingArguments(output_dir="training-output",num_train_epochs=2,per_device_train_batch_size=2,
                       learning_rate=2e-4,logging_steps=1,save_strategy="no",report_to="none")
Trainer(model=model,args=args,train_dataset=ds).train()
model.save_pretrained(out); tok.save_pretrained(out)
size=sum(p.stat().st_size for p in out.rglob("*") if p.is_file())
print(f"Adapter directory: {out.resolve()}\nTotal saved files: {size:,} bytes ({size/1024:.1f} KiB)")
