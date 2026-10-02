# Session 2 - Text Cleaning and Preprocessing

1. Lowercase: `@Priya_Art Lover` becomes `@priya_art lover`.
2. Remove punctuation with `string.punctuation`, retaining letters, digits, and whitespace. For social text, a production pipeline may preserve meaningful `#hashtags` and `@mentions`; this exercise removes punctuation as requested.
3. Tokenize by whitespace after punctuation cleanup. Example: `Fresh paneer tikka tastes great` becomes `['Fresh', 'paneer', 'tikka', 'tastes', 'great']`.
4. Remove English stopwords using NLTK's corpus. Stopword removal is task-dependent: keep negators such as `not` and `no` for sentiment tasks because removing them can reverse meaning.
5. Porter stemming reduces inflected forms to rough roots. It is not linguistically perfect; `#playing` can become `play`, `#dancing` to `danc`, and `#eating` to `eat` after stripping `#`.
