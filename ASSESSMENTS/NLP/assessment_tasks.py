"""Runnable solutions for Module 11 assessment Section B tasks 1-4."""
import re, string
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# A compact fallback keeps this teaching program runnable without a downloaded corpus.
BASIC_STOPWORDS=set("a an the and or but if is are was were be been to of in for on with my your our i it this that not no very".split())
def preprocess(text):
    text=text.lower().translate(str.maketrans("", "", string.punctuation))
    tokens=re.findall(r"\b[a-z]+\b",text)
    # Prefer NLTK's stopwords corpus when installed; preserve negators for sentiment.
    try:
        from nltk.corpus import stopwords
        stops=set(stopwords.words("english"))
    except (ImportError, LookupError): stops=BASIC_STOPWORDS
    stops -= {"not","no","nor"}
    try:
        from nltk.stem import PorterStemmer
        stem=PorterStemmer().stem
    except ImportError: stem=lambda x:x
    return " ".join(stem(w) for w in tokens if w not in stops)

if __name__=="__main__":
    # Task 1: reusable preprocessor, tested on three reviews.
    print("TASK 1 - PREPROCESSOR")
    samples=["Loved the hot pizza!!! Delivered quickly.","Not tasty; food arrived cold and late.","App charged me twice, please help!"]
    for s in samples: print(repr(s),"=>",preprocess(s))

    # Task 2: corpus, labelled full TF-IDF DataFrame, top three words per review.
    print("\nTASK 2 - TF-IDF MATRIX")
    menu_reviews=["Fresh spicy chicken wrap with crisp lettuce","Cold chicken and soggy fries","Delicious paneer bowl with mint chutney","Average burger and ordinary fries","Very spicy noodles, rich flavor","Late delivery and cold pizza","Fresh salad with lemon dressing","Sweet chocolate brownie, excellent dessert"]
    vec=TfidfVectorizer(); matrix=vec.fit_transform(menu_reviews); terms=vec.get_feature_names_out()
    frame=pd.DataFrame(matrix.toarray(),columns=terms,index=[f"review_{i+1}" for i in range(len(menu_reviews))])
    print(frame.round(3).to_string())
    for idx,row in enumerate(matrix.toarray()):
        top=row.argsort()[::-1][:3]
        print(f"review_{idx+1} top:",[(terms[j],round(float(row[j]),3)) for j in top])

    # Task 3: 30 labeled complaint samples across three classes.
    print("\nTASK 3 - COMPLAINT CLASSIFIER")
    delivery=["driver is late","order never arrived","delivery person went to wrong address","tracking has not moved","food came after two hours","driver cannot find my home","order is still out for delivery","delivery was delayed again","missing delivery update","courier did not call"]
    quality=["food arrived cold","pizza was burnt","soup spilled in bag","meal tasted stale","wrong dish was packed","food was undercooked","portion was too small","drink leaked everywhere","meal was tasteless","food quality is poor"]
    app=["app crashes at checkout","payment failed but money deducted","cannot log in to my account","coupon code does not work","screen is stuck loading","order history is missing","app will not accept address","refund status not visible","search feature is broken","notification keeps failing"]
    complaints=delivery+quality+app; labels=["Delivery"]*10+["Food Quality"]*10+["App"]*10
    Xtr,Xte,ytr,yte=train_test_split(complaints,labels,test_size=.2,random_state=21,stratify=labels)
    model=Pipeline([("tfidf",TfidfVectorizer(preprocessor=preprocess,tokenizer=str.split,token_pattern=None)),("nb",MultinomialNB())])
    model.fit(Xtr,ytr); pred=model.predict(Xte)
    print(classification_report(yte,pred,labels=["Delivery","Food Quality","App"],zero_division=0))
    print("Confusion matrix rows=true, columns=predicted [Delivery, Food Quality, App]:")
    print(confusion_matrix(yte,pred,labels=["Delivery","Food Quality","App"]))

    # Task 4: balanced 40-review sentiment dataset and separate model pipelines.
    print("\nTASK 4 - SENTIMENT MODEL COMPARISON")
    pos=["fresh delicious meal","fast delivery and warm food","excellent flavor and portions","loved the tasty biryani","friendly service and great food","perfect pizza arrived hot","wonderful dinner experience","crispy fries and juicy burger","high quality ingredients","quick service and tasty noodles","great value for money","the dessert was amazing","food was packed carefully","best meal this week","pleasant staff and fresh salad","rich flavorful curry","everything tasted excellent","on time and still hot","generous portion and delicious taste","will happily order again"]
    neg=["cold meal arrived very late","food was stale and tasteless","missing items in my order","burnt pizza and soggy fries","terrible delivery experience","small portion and high price","soup leaked in the bag","wrong order and no support","bland food and poor packaging","driver never arrived","disappointing meal overall","the curry was undercooked","order was delayed for hours","bad taste and cold fries","rude service and poor food","overpriced and not fresh","drink spilled everywhere","food arrived damaged","awful flavor and long wait","would not order again"]
    X=pos+neg; y=["Positive"]*len(pos)+["Negative"]*len(neg)
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=17,stratify=y)
    pipelines={"MultinomialNB":Pipeline([("tfidf",TfidfVectorizer(preprocessor=preprocess,tokenizer=str.split,token_pattern=None)),("model",MultinomialNB())]),
               "LogisticRegression":Pipeline([("tfidf",TfidfVectorizer(preprocessor=preprocess,tokenizer=str.split,token_pattern=None)),("model",LogisticRegression(max_iter=1000,class_weight="balanced"))])}
    rows=[]
    for name,pipe in pipelines.items():
        pipe.fit(Xtr,ytr); p=pipe.predict(Xte)
        rows.append({"Model":name,"Accuracy":accuracy_score(yte,p),"Precision_macro":precision_score(yte,p,average="macro",zero_division=0),"Recall_macro":recall_score(yte,p,average="macro",zero_division=0),"F1_macro":f1_score(yte,p,average="macro",zero_division=0)})
    print(pd.DataFrame(rows).set_index("Model").round(3).to_string())
    # Deploy Logistic Regression as a calibrated, flexible baseline after validation; production needs larger data and monitoring.
