# Food Delivery Intelligence Dashboard — Mini Capstone

A multi-page Streamlit app that combines interactive delivery-data exploration
with live Keras ANN demand-prediction inference and model transparency, built
for M9-A1 (Streamlit & Data Apps × Neural Networks & Deep Learning).

## How to run locally

1. Create and activate a virtual environment (recommended):
   `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
2. Install dependencies: `pip install -r requirements.txt`
3. Make sure `demand_model.keras` and `training_history.json` are present in this
   folder (already included; regenerate via `../Section_B/Task3_Order_Demand_Classification_Network/train_classifier.py`
   if you want to retrain).
4. Launch the app: `streamlit run Home.py`
5. Your browser will open at `http://localhost:8501`. Use the sidebar to
   navigate between **Home**, **Data Explorer**, **Demand Predictor**, and
   **Model Info**. On the Data Explorer page you can upload the included
   `sample_delivery_data.csv` to try the app immediately.
