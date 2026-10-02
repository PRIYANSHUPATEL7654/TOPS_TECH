import string
import re


def lowercase(text):
    return text.lower()


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def tokenize(text):
    return text.split()


def remove_stopwords(text, stopwords=None):
    if stopwords is None:
        try:
            from nltk.corpus import stopwords as nltk_stopwords
            stopwords = set(nltk_stopwords.words("english"))
        except LookupError as exc:
            raise RuntimeError("Download NLTK stopwords with: python -m nltk.downloader stopwords") from exc
    # Retain negation because it changes sentiment.
    stopwords = set(stopwords) - {"no", "not", "nor"}
    return " ".join(w for w in text.split() if w.lower() not in stopwords)


def stem_words(words):
    try:
        from nltk.stem import PorterStemmer
    except ImportError as exc:
        raise RuntimeError("Install NLTK: python -m pip install nltk") from exc
    stemmer = PorterStemmer()
    return [(word, stemmer.stem(word.lstrip("#"))) for word in words]

if __name__ == "__main__":
    print(lowercase("My Instagram Bio Is Creative!"))
    print(remove_punctuation("Amazing phone!!! Great camera, worth it."))
    print(tokenize("Fresh paneer tikka tastes great"))
    print(stem_words(["#playing", "#dancing", "#eating"]))
