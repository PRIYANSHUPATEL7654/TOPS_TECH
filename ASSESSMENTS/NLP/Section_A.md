# Module 11 NLP Assessment - Section A

## 1. Support chatbot techniques
Intent classification identifies whether the customer is tracking, cancelling, or reporting a quality issue; entity extraction identifies order IDs, dates, and item names. Without intent classification, messages route to the wrong workflow. Without entity extraction, the bot cannot reliably connect a request to the correct order. A sentiment/urgency signal is also useful, but these two are the core routing needs.

## 2. Preprocessing pipeline
Preserve a raw copy; normalize Unicode; standardize whitespace; case-fold; remove or normalize URLs, punctuation, and markup while preserving meaningful negators and emoji sentiment; tokenize; remove stopwords selectively; optionally stem or lemmatize; then inspect examples and split data before fitting vocabulary/vectorizers. Applying normalization before tokenization makes equivalent spellings consistent; tokenization is required before stopword removal; stemming comes after tokenization. Removing stopwords can reduce noise and dimensionality, but removing `not` can reverse sentiment, so task-aware stopword lists matter.

## 3. BoW vs TF-IDF
Bag of Words stores token counts; TF-IDF scales counts down for words common across the corpus and up for document-specific words. For menu search/ranking, TF-IDF is a reasonable baseline because distinctive terms such as `spicy` or `onion` can become informative. Its limitation: classic TF-IDF does not understand synonyms or word order, so “without onion” may still match “onion” unless negation and phrase logic are added.

## 4. Naive Bayes assumption
Naive Bayes assumes input features are conditionally independent given the class. In a ticket, `cold` and `arrived late` may co-occur because a late delivery causes cold food. Treating them as independent can double-count related evidence and distort probabilities, though the classifier may still work well empirically. If co-occurrence patterns differ between train and production, classification can degrade.

## 5. Imbalanced sentiment evaluation
Prioritize **macro-F1** and **per-class recall** (or balanced accuracy) over raw accuracy. Macro-F1 gives each class equal weight; recall shows whether minority negative reviews are found. Use stratified splitting and class weights or training-only resampling; do not resample the held-out test set.

## 6. Transformer attention and production
Self-attention lets each token compare with other tokens in the sequence in parallel, helping connect distant context more directly than sequential RNN processing. High traffic can cause GPU memory pressure and latency spikes. Common mitigations include batching, quantization, caching, smaller distilled models, autoscaling, and request queues with latency limits.
