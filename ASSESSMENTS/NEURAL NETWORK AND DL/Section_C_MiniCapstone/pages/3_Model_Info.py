"""
Capstone Page — Model Info
Displays the model's architecture summary and training history.
"""

import json

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import tensorflow as tf

st.set_page_config(page_title="Model Info", page_icon="🧠", layout="wide")
st.title("🧠 Model Info")
st.caption("Architecture summary and training history for the demand-classification ANN.")


@st.cache_resource
def load_model():
    return tf.keras.models.load_model("demand_model.keras")


try:
    model = load_model()
except Exception as e:
    st.error(f"⚠️ Could not load demand_model.keras: {e}")
    st.stop()

# ---------------------------------------------------------------------------
# Architecture summary as a formatted table
# ---------------------------------------------------------------------------
st.subheader("Architecture Summary")

rows = []
total_params = 0
for layer in model.layers:
    try:
        out_shape = layer.output_shape
    except Exception:
        out_shape = "N/A"
    params = layer.count_params()
    total_params += params
    rows.append(
        {
            "Layer (type)": f"{layer.name} ({layer.__class__.__name__})",
            "Output Shape": str(out_shape),
            "Parameters": f"{params:,}",
        }
    )

summary_df = pd.DataFrame(rows)
st.dataframe(summary_df, use_container_width=True, hide_index=True)
st.metric("Total Parameters", f"{total_params:,}")

st.divider()

# ---------------------------------------------------------------------------
# Training history charts
# ---------------------------------------------------------------------------
st.subheader("Training History")

try:
    with open("training_history.json") as f:
        history = json.load(f)

    epochs = list(range(1, len(history["accuracy"]) + 1))

    acc_fig = go.Figure()
    acc_fig.add_trace(go.Scatter(x=epochs, y=history["accuracy"], mode="lines", name="Training Accuracy"))
    acc_fig.add_trace(go.Scatter(x=epochs, y=history["val_accuracy"], mode="lines", name="Validation Accuracy"))
    acc_fig.update_layout(title="Accuracy over Epochs", xaxis_title="Epoch", yaxis_title="Accuracy")
    st.plotly_chart(acc_fig, use_container_width=True)

    loss_fig = go.Figure()
    loss_fig.add_trace(go.Scatter(x=epochs, y=history["loss"], mode="lines", name="Training Loss"))
    loss_fig.add_trace(go.Scatter(x=epochs, y=history["val_loss"], mode="lines", name="Validation Loss"))
    loss_fig.update_layout(title="Loss over Epochs", xaxis_title="Epoch", yaxis_title="Loss")
    st.plotly_chart(loss_fig, use_container_width=True)

    col1, col2 = st.columns(2)
    col1.metric("Final Test Accuracy", f"{history['test_accuracy']*100:.2f}%")
    col2.metric("Final Test Loss", f"{history['test_loss']:.4f}")

except FileNotFoundError:
    st.warning(
        "training_history.json not found. Re-run the Task 3 training script "
        "(with history export) and copy it into this folder to populate these charts."
    )
