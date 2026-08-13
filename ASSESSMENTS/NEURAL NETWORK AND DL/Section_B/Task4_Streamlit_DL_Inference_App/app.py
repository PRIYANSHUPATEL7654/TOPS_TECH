"""
Task 4 — Streamlit Deep Learning Inference App
Section B — Integrative (Streamlit + Keras + Plotly)

Prerequisite: demand_model.keras must exist in this folder
              (copied from Task 3, or run Task 3's train_classifier.py here).
Run with:      streamlit run app.py
"""

import numpy as np
import plotly.graph_objects as go
import streamlit as st
import tensorflow as tf

st.set_page_config(page_title="Demand Prediction", layout="centered")

st.title("📈 Food Delivery Demand Predictor")
st.caption("Live inference using the Keras ANN trained in Task 3.")

CLASS_NAMES = ["Low", "Medium", "High"]
DAY_MAP = {
    "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
    "Friday": 4, "Saturday": 5, "Sunday": 6,
}

# ---------------------------------------------------------------------------
# Requirement 1 — Load & cache the trained Keras model
# ---------------------------------------------------------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("demand_model.keras")


model_loaded = True
try:
    model = load_model()
except Exception as e:
    model = None
    model_loaded = False
    st.error(
        "⚠️ Could not load demand_model.keras. "
        f"Details: {e}\n\nRun Task 3's train_classifier.py first to generate the model file."
    )

# ---------------------------------------------------------------------------
# Requirement 2 — Input widgets
# ---------------------------------------------------------------------------
hour = st.slider("Hour of Day", min_value=0, max_value=23, value=13)
day_name = st.selectbox("Day of Week", list(DAY_MAP.keys()))
temperature = st.number_input("Temperature (°C)", min_value=10.0, max_value=45.0, value=28.0, step=0.5)

# ---------------------------------------------------------------------------
# Requirement 3 & 4 — Predict + Plotly confidence bar chart
# ---------------------------------------------------------------------------
if st.button("Predict Demand", type="primary", disabled=not model_loaded):
    try:
        day_encoded = DAY_MAP[day_name]

        # Same scaling used in training (train_classifier.py)
        hour_scaled = hour / 23.0
        day_scaled = day_encoded / 6.0
        temp_scaled = (temperature - 10) / (45 - 10)

        features = np.array([[hour_scaled, day_scaled, temp_scaled]], dtype="float32").reshape(1, 3)

        probs = model.predict(features, verbose=0)[0]
        pred_idx = int(np.argmax(probs))
        pred_class = CLASS_NAMES[pred_idx]
        confidence = probs[pred_idx] * 100

        message = f"Predicted demand: **{pred_class}** ({confidence:.1f}% confidence)"
        if pred_class == "High":
            st.warning(f"🔴 {message}")
        else:
            st.success(f"🟢 {message}")

        fig = go.Figure(
            data=[
                go.Bar(
                    x=CLASS_NAMES,
                    y=[float(p) for p in probs],
                    marker_color=["#4C9AFF", "#FFAB00", "#DE350B"],
                    text=[f"{p*100:.1f}%" for p in probs],
                    textposition="auto",
                )
            ]
        )
        fig.update_layout(
            title="Prediction Confidence by Class",
            yaxis_title="Probability",
            xaxis_title="Demand Class",
            yaxis=dict(range=[0, 1]),
        )
        st.plotly_chart(fig, use_container_width=True)

    except ValueError as ve:
        st.error(f"Invalid input: {ve}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
