# Session 1 - Introduction to NLP and Use Cases

## 1. What NLP is
Natural Language Processing (NLP) is the area of computing that helps software work with human language. It combines language rules and machine learning so an app can classify, search, translate, summarize, or respond to text. A daily example is a messaging app detecting likely spam from the words and patterns in a message.

## 2. Three ways NLP improves apps
1. **Intent detection:** Recognizes whether a customer wants to track, change, or cancel an order, routing them to the right action.
2. **Sentiment and emotion analysis:** Finds dissatisfaction or urgency in a review so support can prioritize a problem.
3. **Information extraction and search:** Identifies entities such as order numbers, locations, products, and dates, helping users find relevant information without exact wording.

## 3. Tokenization
For `I love ordering pizza from Zomato!`, Python's `split()` returns `['I', 'love', 'ordering', 'pizza', 'from', 'Zomato!']`. `split()` separates on whitespace; it does not remove punctuation.

## 4. Basic sentiment checker
The script checks lowercased text for the words `good` and `bad`. It is a teaching baseline: keyword matching misses negation such as “not good” and context such as “bad service but great food.”

## 5. Spam detector
The function returns `True` if a case-insensitive whole-word `win` or `free` occurs. Whole-word matching avoids triggering on a word such as `freezer`.
