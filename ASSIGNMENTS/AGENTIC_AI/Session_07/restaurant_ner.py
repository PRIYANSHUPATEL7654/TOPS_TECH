"""Local restaurant-name spotting. Uses spaCy NER when installed; safe dictionary fallback."""
import re
KNOWN={"Barbeque Nation","Domino's","Dominos"}
def detect_restaurants(messages):
    try:
        import spacy
        nlp=spacy.load("en_core_web_sm")
        names=[]
        for message in messages:
            doc=nlp(message)
            names.extend(ent.text for ent in doc.ents if ent.label_=="ORG" and any(k.casefold() in ent.text.casefold() for k in ("Domino","Barbeque Nation")))
        if names: return sorted(set(names))
    except (ImportError, OSError): pass
    text=" ".join(messages).casefold()
    return sorted({name for name in KNOWN if name.casefold() in text},key=str.casefold)
if __name__=="__main__":
    reviews=["Great delivery from Barbeque Nation", "Domino's pizza arrived warm", "Loved the restaurant"]
    print(detect_restaurants(reviews))
