# Session 5 - Deep Learning for NLP

Traditional Bag of Words and TF-IDF represent tokens largely without word order or context. For example, “not good” and “good” can look similar unless negation is modeled explicitly; synonyms may also have unrelated vectors.

A transformer model used for text classification besides BERT is **DistilBERT**. It is a smaller, distilled Transformer designed to retain much of BERT's language understanding with fewer parameters and faster inference. Another widely used option is RoBERTa, which changes BERT's pretraining recipe.

A Hugging Face sentiment pipeline is included in `sentiment_pipeline.py`. The three review strings are illustrative examples, not copied from current Zomato/Swiggy reviews. The attention demo computes scaled dot-product attention over three short sentence embeddings; a score indicates how strongly a query vector weights each key. It is a transparent toy calculation, not a trained language model's full attention visualization.

## Version check task
Run `python versions.py` after installing `transformers` and `torch` to display their installed version numbers.
