# NLP Assessment Submission

## Included sections
- `Section_A.md`: scenario-based concept responses.
- `assessment_tasks.py`: four practical tasks (preprocessing, TF-IDF, Naive Bayes complaints, and NB/Logistic Regression comparison).
- `capstone.py` and `reviews.json`: interactive review-intelligence application and starter labeled records.
- `Section_D_AI_Learning.md` and `section_d_corrected.py`: exact prompt, preserved baseline, correction note, and corrected executable program.

## Run
Install the root `requirements.txt`, then run:

```bash
python assessment_tasks.py
python capstone.py
python section_d_corrected.py
```

For the capstone, choose option 1 to add labeled examples before option 2. Classification requires at least six labeled samples covering at least two labels in each classifier. The included records meet that threshold. Data is stored in `reviews.json`.
