# Install with: python -m pip install transformers torch
from transformers import pipeline

reviews=[
    "The thali was delicious, warm, and delivered quickly.",
    "My order arrived cold and the packaging was damaged.",
    "The restaurant has a wide menu and average prices."
]
classifier=pipeline("sentiment-analysis",model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
for review,result in zip(reviews,classifier(reviews)):
    print(f"{review}\n  {result['label']} ({result['score']:.3f})")
