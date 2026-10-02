# Session 3 - Feature Engineering for Text

## Vocabulary from three sample captions
Captions: “Rainy day reads 📚”, “Reading by the window”, “Books, coffee, and rain!” After case-folding and punctuation removal, the unique vocabulary is: `rainy, day, reads, reading, by, the, window, books, coffee, and, rain`.

## Bag of Words and word frequency
The script creates a CountVectorizer matrix for three short restaurant reviews and separately counts non-stopword tokens across sample chat messages. Bag of Words records term counts and ignores order.

## TF-IDF
TF-IDF downweights terms appearing in many documents and highlights terms more specific to one review. The script prints the score for `quality` in every review; a zero means that exact vocabulary term is absent from that document.

## When TF-IDF is preferable
For searching product reviews, TF-IDF can make a distinctive word such as `waterproof` count more than a generic word such as `good`. Bag of Words is simpler and often useful with a classifier, but gives common and rare terms equal raw-count status. Both methods lose word order and deeper meaning.
