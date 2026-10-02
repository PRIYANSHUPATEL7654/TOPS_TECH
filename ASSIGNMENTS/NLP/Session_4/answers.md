# Session 4 - Text Classification Models

The included sample CSV is a small, clearly labeled teaching dataset. It is not a scrape of recent IPL posts. Replace it with a permitted CSV export when using real posts, and inspect the schema before training.

The script shows how to load a CSV with pandas, print its first ten rows, train Multinomial Naive Bayes and Logistic Regression for review sentiment, classify three sample WhatsApp-style messages, and compare accuracy on one fixed stratified split. Accuracy alone is not enough for imbalanced data; inspect per-class precision, recall, and F1 as well. With a tiny dataset, scores are illustrative and unstable.

The final section gives the prompt used for the AI-assisted Flipkart classifier, the code is included in `ai_review_classifier.py`, and two test predictions are printed. No claim is made that a tiny sample is production quality.
