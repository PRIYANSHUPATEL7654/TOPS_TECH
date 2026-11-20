"""Session 2 Task 2 - sentiment of a Zomato review using a BERT model.   pip install transformers torch
NOTE: plain 'bert-base-uncased' has no sentiment head (it is only pre-trained), so we load a BERT-base-uncased
checkpoint that was fine-tuned on SST-2 sentiment data. If it cannot be downloaded we fall back to the
pipeline's default model."""
from transformers import pipeline

review = "The food was absolutely delicious and the delivery was super fast."
try:
    clf = pipeline("sentiment-analysis", model="textattack/bert-base-uncased-SST-2")
    label_map = {"LABEL_0": "NEGATIVE", "LABEL_1": "POSITIVE"}
except Exception:
    clf = pipeline("sentiment-analysis")
    label_map = {}
res = clf(review)[0]
print("Review   :", review)
print("Sentiment: %s (confidence %.3f)" % (label_map.get(res["label"], res["label"]), res["score"]))
