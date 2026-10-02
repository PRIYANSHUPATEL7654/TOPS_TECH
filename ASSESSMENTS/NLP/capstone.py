"""Console-based Food Delivery Review Intelligence System."""
from collections import Counter
from pathlib import Path
import json, re
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

DATA=Path(__file__).with_name("reviews.json")
STOP=set("a an the and or but is are was were to of in for on with i it this that my very".split())-{"not","no"}
def clean(s):
    tokens=re.findall(r"[a-z]+",s.lower())
    try:
        from nltk.corpus import stopwords
        stops=set(stopwords.words("english"))-{"not","no","nor"}
    except (ImportError,LookupError): stops=STOP
    try:
        from nltk.stem import PorterStemmer
        stem=PorterStemmer().stem
    except ImportError: stem=lambda w:w
    return " ".join(stem(w) for w in tokens if w not in stops)

def load():
    try:return json.loads(DATA.read_text(encoding="utf-8"))
    except (FileNotFoundError,json.JSONDecodeError):return []
def save(rows): DATA.write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding="utf-8")

def train(rows,key):
    labeled=[r for r in rows if r.get(key) in ("Positive","Negative") if key=="sentiment"] if key=="sentiment" else [r for r in rows if r.get(key) in ("Delivery","Food Quality","App","General")]
    if len(labeled)<6 or len(set(r[key] for r in labeled))<2: return None
    m=Pipeline([("tfidf",TfidfVectorizer()),("clf",LogisticRegression(max_iter=1000,class_weight="balanced"))])
    m.fit([r["processed"] for r in labeled],[r[key] for r in labeled]);return m

def classify(text,rows):
    processed=clean(text)
    sm=train(rows,"sentiment"); cm=train(rows,"category")
    if sm is None or cm is None: return None,"At least 6 labeled examples covering at least two labels per classifier are needed. Add reviews with labels first."
    return {"sentiment":sm.predict([processed])[0],"category":cm.predict([processed])[0],"processed":processed},None

def summary(rows):
    print("Total reviews:",len(rows))
    print("Sentiment counts:",dict(Counter(r.get("sentiment","Unlabeled") for r in rows)))
    print("Issue category counts:",dict(Counter(r.get("category","Unlabeled") for r in rows)))
    words=Counter(w for r in rows for w in r.get("processed","").split())
    print("Top 5 content words:",words.most_common(5))

def main():
    rows=load()
    while True:
        print("\n1 Add a labeled review\n2 Classify a new review\n3 Summary report\n4 Exit")
        choice=input("Choose: ").strip()
        if choice=="1":
            text=input("Review: ").strip()
            if not text: print("Review cannot be empty.");continue
            sent=input("Known sentiment (Positive/Negative): ").strip().title()
            cat=input("Known issue category (Delivery/Food Quality/App/General): ").strip().title()
            if sent not in {"Positive","Negative"} or cat not in {"Delivery","Food Quality","App","General"}:
                print("Invalid label; review not stored.");continue
            rows.append({"raw":text,"processed":clean(text),"sentiment":sent,"category":cat});save(rows);print("Review stored.")
        elif choice=="2":
            text=input("Review to classify: ").strip()
            if not text: print("Review cannot be empty.");continue
            result,error=classify(text,rows)
            print(error if error else f"Sentiment: {result['sentiment']} | Issue category: {result['category']} | Processed: {result['processed']}")
        elif choice=="3": summary(rows)
        elif choice=="4": break
        else: print("Choose 1, 2, 3, or 4.")
if __name__=="__main__":main()
