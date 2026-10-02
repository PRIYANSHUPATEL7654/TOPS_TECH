from collections import Counter
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

captions = ["Rainy day reads 📚", "Reading by the window", "Books, coffee, and rain!"]
words = set()
for caption in captions:
    words.update(re.findall(r"[a-z0-9]+", caption.lower()))
print("Unique caption vocabulary:", sorted(words))

reviews = ["Loved the pizza", "Service was slow", "Great ambience"]
cv = CountVectorizer()
counts = cv.fit_transform(reviews)
print("\nBag of Words:")
print(pd.DataFrame(counts.toarray(), columns=cv.get_feature_names_out(), index=[f"review_{i+1}" for i in range(len(reviews))]))

messages = ["the order is at the door", "is the order at reception", "food is at the door"]
stop = {"the", "is", "at"}
frequencies = Counter(w for m in messages for w in re.findall(r"[a-z]+", m.lower()) if w not in stop)
print("\nNon-stopword message counts:", dict(frequencies))

product_reviews = ["The screen quality is excellent", "Poor quality packaging", "Quality camera and battery"]
tfidf = TfidfVectorizer()
mat = tfidf.fit_transform(product_reviews)
terms = tfidf.get_feature_names_out()
print("\nTF-IDF score for 'quality':")
for i, row in enumerate(mat.toarray(), start=1):
    score = row[list(terms).index("quality")] if "quality" in terms else 0.0
    print(f"review_{i}: {score:.4f}")
