"""LoRA adapter parameter count for a DistilBERT sentiment classifier.
Run after installing requirements and allowing the model download.
"""
from transformers import AutoModelForSequenceClassification
from peft import LoraConfig, TaskType, get_peft_model

MODEL="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
model=AutoModelForSequenceClassification.from_pretrained(MODEL)
def count(m): return sum(p.numel() for p in m.parameters() if p.requires_grad)
print("Trainable parameters before LoRA:",count(model))
config=LoraConfig(task_type=TaskType.SEQ_CLS,r=8,lora_alpha=16,lora_dropout=.1,
                  target_modules=["q_lin","v_lin"],modules_to_save=["pre_classifier","classifier"])
peft_model=get_peft_model(model,config)
print("Trainable parameters after LoRA:",count(peft_model))
peft_model.print_trainable_parameters()
