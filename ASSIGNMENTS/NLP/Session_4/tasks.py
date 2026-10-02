from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

ROOT = Path(__file__).parent
print("Sample IPL tweet data (teaching data):")
print(pd.read_csv(ROOT / "ipl_tweets_sample.csv").head(10).to_string(index=False))

reviews = [
("Loved the fresh food and quick delivery", "positive"), ("Amazing taste and friendly staff", "positive"),
("Hot meal arrived right on time", "positive"), ("Excellent packaging and generous portions", "positive"),
("The biryani was flavorful and delicious", "positive"), ("Great service, I will order again", "positive"),
("Very tasty pizza and fast service", "positive"), ("Perfect dinner, everything was fresh", "positive"),
("Cold food arrived an hour late", "negative"), ("The order was missing two items", "negative"),
("Terrible taste and leaking package", "negative"), ("Driver never delivered my meal", "negative"),
("Food was stale and overpriced", "negative"), ("App charged me but order failed", "negative"),
("Worst experience, support did not help", "negative"), ("The soup spilled everywhere", "negative"),
("Good portion and nice flavor", "positive"), ("Quick delivery and warm food", "positive"),
("Wrong order and no refund", "negative"), ("Disappointing meal, tasted old", "negative")]
X=[x for x,y in reviews]; y=[y for x,y in reviews]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
models={"Naive Bayes":make_pipeline(TfidfVectorizer(),MultinomialNB()),"Logistic Regression":make_pipeline(TfidfVectorizer(),LogisticRegression(max_iter=1000))}
for name,m in models.items():
    m.fit(Xtr,ytr); print(name,"accuracy:",round(accuracy_score(yte,m.predict(Xte)),3))

spam_data=[("claim your free prize now","spam"),("win cash by clicking here","spam"),("urgent free voucher","spam"),("you have won a gift card","spam"),("claim reward now","spam"),("free entry contest today","spam"),("limited offer win big","spam"),("click to claim your prize","spam"),("team meeting at ten","not spam"),("please send the report","not spam"),("are we still meeting today","not spam"),("your order is on the way","not spam"),("thanks for your help","not spam"),("call me when you arrive","not spam"),("the class starts at noon","not spam"),("I shared the project file","not spam")]
spam=make_pipeline(TfidfVectorizer(),LogisticRegression(max_iter=1000)).fit([a for a,b in spam_data],[b for a,b in spam_data])
for msg in ["Free voucher claim now","Can we meet after class","Your package arrives tomorrow"]: print("Message:",msg,"=>",spam.predict([msg])[0])

# AI-assisted code prompt: "Create a short Python example that trains a TF-IDF plus LogisticRegression
# sentiment classifier on labeled product reviews and predicts two new reviews. Keep it runnable and
# include a train/test split and accuracy."
