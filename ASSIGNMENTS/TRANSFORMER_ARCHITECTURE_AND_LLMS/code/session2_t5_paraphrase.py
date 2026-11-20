"""Session 2 Task 3 - paraphrase with T5-base.   pip install transformers torch sentencepiece"""
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

sentence = "BookMyShow makes movie ticket booking easy and fast."
inputs = tokenizer("paraphrase: " + sentence, return_tensors="pt", truncation=True)
ids = model.generate(**inputs, max_length=40, num_beams=5, repetition_penalty=2.0, early_stopping=True)
print("Original  :", sentence)
print("Paraphrase:", tokenizer.decode(ids[0], skip_special_tokens=True))
