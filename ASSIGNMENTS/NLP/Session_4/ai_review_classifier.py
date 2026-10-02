from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

texts=["excellent battery and clear display","fast phone with a bright screen","great value and smooth performance","camera takes beautiful photos","battery lasts all day","easy to use and premium feel","poor battery drains quickly","screen is dull and scratched","slow phone with weak camera","bad quality and frequent crashes","overheats and freezes","not worth the price"]
labels=["positive"]*6+["negative"]*6
X_train,X_test,y_train,y_test=train_test_split(texts,labels,test_size=.25,random_state=7,stratify=labels)
model=make_pipeline(TfidfVectorizer(ngram_range=(1,2)),LogisticRegression(max_iter=1000,class_weight="balanced"))
model.fit(X_train,y_train)
print("Holdout accuracy:",round(accuracy_score(y_test,model.predict(X_test)),3))
for review in ["Excellent screen and battery", "Terrible phone, it freezes"]:
    print(review,"=>",model.predict([review])[0])
