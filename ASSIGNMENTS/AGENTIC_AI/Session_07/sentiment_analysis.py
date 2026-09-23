"""Optional Hugging Face sentiment classification for sample food reviews."""
def analyze_reviews(reviews):
    try:
        from transformers import pipeline
    except ImportError:
        return [(text, "sample/unclassified", "Install transformers and torch for model inference") for text in reviews]
    classifier=pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
    results=classifier(reviews)
    return [(text, "positive" if result["label"]=="POSITIVE" else "negative", round(result["score"],3)) for text,result in zip(reviews,results)]
if __name__=="__main__":
    sample=["Great food and quick delivery!", "The order was cold and late.", "The meal arrived at 7 pm."]
    for row in analyze_reviews(sample): print(row)
