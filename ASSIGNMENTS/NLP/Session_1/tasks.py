import re

sentence = "I love ordering pizza from Zomato!"
print("Tokens:", sentence.split())

def sentiment(review: str) -> str:
    words = set(re.findall(r"\b[\w']+\b", review.lower()))
    if "good" in words and "bad" not in words:
        return "Positive"
    if "bad" in words and "good" not in words:
        return "Negative"
    return "Neutral"


def is_spam(email_text: str) -> bool:
    return bool(re.search(r"\b(win|free)\b", email_text, flags=re.IGNORECASE))

if __name__ == "__main__":
    review = input("Enter a movie review: ").strip()
    print("Sentiment:", sentiment(review) if review else "Neutral")
    print("Spam example 1:", is_spam("You may win a free phone"))
    print("Spam example 2:", is_spam("Meeting notes attached"))
