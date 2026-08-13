# Assessment Submission — Data Science (Streamlit & Data Apps × Neural Networks & Deep Learning)

This archive contains a complete, runnable submission for all four sections of
the assessment.

## Contents

```
Section_A_Concept_Answers.txt         Written answers to Section A (S1–S6)

Section_B/
  Task1_Delivery_Summary_Dashboard/   Streamlit app.py + sample_delivery_data.csv
  Task2_Delivery_Time_Prediction_UI/  train_model.py, app.py, delivery_model.pkl
  Task3_Order_Demand_Classification_Network/
                                       train_classifier.py, demand_model.keras,
                                       training_history.png/.json, training_output.txt
  Task4_Streamlit_DL_Inference_App/   app.py, demand_model.keras

Section_C_MiniCapstone/               Multi-page Streamlit app (Home + 3 pages),
                                       requirements.txt, README.md, model + sample data

Section_D_AI_Augmented/               prompt_used.txt, ai_original_code.py (buggy),
                                       corrected_code.py (fixed), explanation_note.txt,
                                       loss-curve PNGs and run logs from both versions
```

## How to run any Streamlit app

1. `pip install -r requirements.txt` (a combined list is below; each subfolder
   also documents its own dependencies).
2. `cd` into the relevant task folder.
3. Run `streamlit run app.py` (or `streamlit run Home.py` for the Section C
   capstone).
4. Take a screenshot of the running app in your browser (`localhost:8501`) as
   required by the assessment's submission instructions — this wasn't
   possible to auto-generate here since it requires an interactive browser
   session, but every app has already been built, and its underlying model
   trained and verified to run correctly (see the `training_output.txt`,
   `training_history.png`, and log files included for the deep-learning
   tasks, which satisfy the "training output and evaluation metrics"
   requirement).

## Combined requirements.txt

```
streamlit>=1.35
pandas>=2.0
numpy>=1.26
matplotlib>=3.8
plotly>=5.20
scikit-learn>=1.4
joblib>=1.3
tensorflow-cpu>=2.16
```

## Notes on models

- `Section_B/Task2.../delivery_model.pkl` — a `RandomForestRegressor` trained
  on synthetic distance/order-value/time-of-day data (R² ≈ 0.97 on held-out
  test data). Regenerate anytime with `python train_model.py`.
- `demand_model.keras` (used by Task 3, Task 4, and the Section C capstone) —
  a Keras Sequential ANN (Dense 64 → Dropout 0.3 → Dense 32 → Dropout 0.3 →
  Dense 3 softmax) trained on synthetic hour/day/temperature data for 30
  epochs. Regenerate with `python train_classifier.py` inside
  `Section_B/Task3_Order_Demand_Classification_Network/`.
- All datasets are synthetically generated inside the scripts themselves so
  every task is fully self-contained and reproducible.

## Section D

`Section_D_AI_Augmented` documents the full AI-augmented workflow: the exact
prompt given to Claude, the AI's original (buggy) code, the actual bug found
by manual testing (sigmoid + MSE loss used for a 3-class softmax problem,
producing invalid probability outputs that don't sum to 1 and depressed
validation accuracy), the hand-corrected version (softmax +
categorical_crossentropy), and a short note explaining the fix — along with
real run logs and loss-curve plots from both versions for comparison.
