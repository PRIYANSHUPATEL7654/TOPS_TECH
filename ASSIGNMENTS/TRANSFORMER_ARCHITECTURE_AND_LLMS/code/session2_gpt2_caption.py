"""Session 2 Task 1 - GPT-2 Instagram-style caption.   pip install transformers torch"""
from transformers import pipeline, set_seed

set_seed(42)
generator = pipeline("text-generation", model="gpt2")
prompt = "Sunset vibes at the beach"
out = generator(prompt, max_new_tokens=25, num_return_sequences=1, do_sample=True, temperature=0.9, truncation=True)
print("Caption:", out[0]["generated_text"].strip())
