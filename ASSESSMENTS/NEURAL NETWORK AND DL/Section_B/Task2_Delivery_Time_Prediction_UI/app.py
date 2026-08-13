"""
Task 2 — Delivery Time Prediction UI
Section B, Module 8 (Streamlit)

Prerequisite: run `python train_model.py` once to generate delivery_model.pkl
Run with:      streamlit run app.py
"""

import joblib
import numpy as np
import streamlit as st

st.set_page_config(page_title="Delivery Time Predictor", layout="centered")

st.title("⏱️ Delivery Time Prediction")
st.caption("Enter order details to get an instant estimated delivery time.")

TIME_OF_DAY_MAP = {"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3}

# ---------------------------------------------------------------------------
# Requirement 1 — Cached model loader
# ---------------------------------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("delivery_model.pkl")


try:
    model = load_model()
    model_loaded = True
except Exception as e:  # file missing / corrupt / joblib error
    model = None
    model_loaded = False
    st.error(
        "⚠️ Could not load the prediction model (delivery_model.pkl). "
        f"Details: {e}\n\nRun `python train_model.py` first to generate it."
    )

# ---------------------------------------------------------------------------
# Requirement 2 — Input widgets
# ---------------------------------------------------------------------------
distance = st.slider("Distance from restaurant (km)", min_value=1, max_value=50, value=5)
order_value = st.number_input("Order Value (Rs)", min_value=0.0, value=350.0, step=10.0)
time_of_day = st.selectbox("Time of Day", list(TIME_OF_DAY_MAP.keys()))

# ---------------------------------------------------------------------------
# Requirement 3 & 4 — Predict button + try/except handling
# ---------------------------------------------------------------------------
if st.button("Predict Delivery Time", type="primary", disabled=not model_loaded):
    try:
        if order_value < 0 or distance <= 0:
            raise ValueError("Distance and order value must be positive numbers.")

        encoded_time = TIME_OF_DAY_MAP[time_of_day]
        features = np.array([[distance, order_value, encoded_time]])

        prediction = model.predict(features)[0]
        st.success(f"✅ Estimated delivery time: **{prediction:.1f} minutes**")

    except ValueError as ve:
        st.error(f"Invalid input: {ve}")
    except Exception as e:
        st.error(f"Something went wrong while generating the prediction: {e}")
