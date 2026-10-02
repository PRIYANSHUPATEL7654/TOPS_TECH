"""Quantized LoRA training with actual process/GPU memory telemetry.
Requires a compatible CUDA GPU, bitsandbytes, transformers, peft, datasets, accelerate, psutil.
"""
from pathlib import Path
import csv, os, time
try:
    import psutil, torch
    from datasets import Dataset
    from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer, BitsAndBytesConfig
    from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
except ImportError as e:
    raise SystemExit(f"Missing dependency: {e}. Install the optional fine-tuning requirements first.")
if not torch.cuda.is_available():
    raise SystemExit("QLoRA benchmark needs a CUDA GPU and a supported bitsandbytes build; no memory result was recorded.")

MODEL="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
texts=["fresh and delicious meal","excellent quick delivery","wonderful flavor","loved this order",
       "cold food arrived late","missing items and poor service","bad taste","very disappointing"]
labels=[1,1,1,1,0,0,0,0]
tok=AutoTokenizer.from_pretrained(MODEL)
ds=Dataset.from_dict({"text":texts,"labels":labels}).map(lambda b:tok(b["text"],truncation=True,padding="max_length",max_length=96),batched=True).remove_columns(["text"])
quant=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type="nf4",bnb_4bit_use_double_quant=True,bnb_4bit_compute_dtype=torch.float16)
model=AutoModelForSequenceClassification.from_pretrained(MODEL,quantization_config=quant,device_map="auto")
model=prepare_model_for_kbit_training(model)
model=get_peft_model(model,LoraConfig(task_type=TaskType.SEQ_CLS,r=4,lora_alpha=8,lora_dropout=.1,target_modules=["q_lin","v_lin"],modules_to_save=["pre_classifier","classifier"]))
torch.cuda.reset_peak_memory_stats(); proc=psutil.Process(os.getpid()); start=time.time()
args=TrainingArguments(output_dir="qlora-output",num_train_epochs=1,per_device_train_batch_size=2,gradient_accumulation_steps=1,
                       learning_rate=2e-4,save_strategy="no",logging_steps=1,report_to="none",fp16=True)
Trainer(model=model,args=args,train_dataset=ds).train()
elapsed=time.time()-start
row={"method":"4-bit QLoRA","peak_process_rss_mib":round(proc.memory_info().peak_wset/1024**2 if hasattr(proc.memory_info(),"peak_wset") else proc.memory_info().rss/1024**2,2),
     "peak_cuda_allocated_mib":round(torch.cuda.max_memory_allocated()/1024**2,2),"peak_cuda_reserved_mib":round(torch.cuda.max_memory_reserved()/1024**2,2),"seconds":round(elapsed,1)}
with open("qlora_memory_results.csv","w",newline="") as f: w=csv.DictWriter(f,fieldnames=row); w.writeheader(); w.writerow(row)
print(row); print("To compare standard fine-tuning, run an otherwise identical full-precision baseline and record the same fields.")
