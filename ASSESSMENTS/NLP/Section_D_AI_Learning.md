# Section D - AI-Augmented Learning Evidence

## Item 1: Exact prompt used
“Create a beginner-friendly Python program for food-delivery review sentiment classification. Use at least 20 labeled reviews, lowercase and tokenize text, remove English stopwords while preserving ‘not’, stem tokens with NLTK PorterStemmer, transform text with TF-IDF, split into train and test sets using stratification, train Logistic Regression, print accuracy, and let a user enter three new reviews one by one. Include dependency notes and handle missing NLTK data clearly.”

## Item 2a: AI's original code
The original baseline below follows the requested steps but contains a leakage flaw: it fits the TF-IDF vectorizer on the complete dataset before splitting, allowing test vocabulary to influence training features. It also uses a tiny dataset and does not handle NLTK corpus absence.

```python
# ORIGINAL AI-GENERATED BASELINE (intentionally preserved for comparison)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

reviews = ["great food", "loved the meal", "excellent delivery", "tasty and fresh",
           "bad food", "cold and late", "terrible taste", "missing order"]
labels = [1,1,1,1,0,0,0,0]
stop = set(stopwords.words("english"))
stemmer = PorterStemmer()
def preprocess(text):
    return " ".join(stemmer.stem(w) for w in re.findall(r"\b[a-z]+\b", text.lower()) if w not in stop)
cleaned = [preprocess(x) for x in reviews]
X = TfidfVectorizer().fit_transform(cleaned)  # flaw: learns vocabulary before split
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=.25, random_state=42)
model = LogisticRegression().fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
for _ in range(3):
    text = input("Review: ")
    print("Positive" if model.predict(TfidfVectorizer().fit_transform([preprocess(text)]))[0] == 1 else "Negative")
```

## Item 2b: Corrected version
The corrected `section_d_corrected.py` contains a larger balanced sample, preserves negation, uses a single scikit-learn Pipeline so vectorization is fitted only on training data, stratifies the split, reuses the fitted pipeline for inference, and prompts for three new reviews.

## Item 3: Change note
The original code fit TF-IDF before the train/test split, leaking test vocabulary into training, and then created a new vectorizer for each user review, so prediction features did not match the model's training features. I moved preprocessing/vectorization/modeling into one Pipeline fitted only on the training split and reused it for all predictions. I also preserved negation and added more balanced examples so the demonstration is less brittle.
