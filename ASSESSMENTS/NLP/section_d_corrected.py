"""Corrected Section D program. Run: python section_d_corrected.py"""
import re
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

texts=["great food and quick delivery","loved the fresh meal","excellent flavor and service","hot tasty pizza","wonderful dinner","friendly staff and delicious food","fast delivery and warm meal","perfect order","good portion and taste","fresh salad and great dressing","bad food and slow service","cold meal arrived late","terrible taste","missing items again","disappointing dinner","burnt pizza and soggy fries","awful delivery experience","stale food and poor packaging","wrong order and no help","not worth the price"]
labels=["Positive"]*10+["Negative"]*10
Xtr,Xte,ytr,yte=train_test_split(texts,labels,test_size=.25,random_state=42,stratify=labels)
# Tokenization is handled by the vectorizer; negation is deliberately retained.
model=Pipeline([("tfidf",TfidfVectorizer(lowercase=True,ngram_range=(1,2),stop_words=None)),("classifier",LogisticRegression(max_iter=1000,class_weight="balanced"))])
model.fit(Xtr,ytr)
print(f"Holdout accuracy: {accuracy_score(yte,model.predict(Xte)):.3f}")
print("Enter three reviews:")
for i in range(3):
    review=input(f"Review {i+1}: ").strip()
    if not review: print("Please enter text; prediction skipped.");continue
    print("Predicted sentiment:",model.predict([review])[0])
