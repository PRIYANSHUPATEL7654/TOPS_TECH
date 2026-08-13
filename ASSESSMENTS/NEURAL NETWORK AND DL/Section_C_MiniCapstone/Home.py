"""
Mini Capstone — Food Delivery Intelligence Dashboard
Section C

Entry point of the multi-page Streamlit app.
Run with:  streamlit run Home.py
Pages live in ./pages and are auto-discovered by Streamlit's
sidebar navigation (Data Explorer, Demand Predictor, Model Info).
"""

import streamlit as st

st.set_page_config(page_title="Food Delivery Intelligence Dashboard", page_icon="🚴", layout="wide")

st.title("🚴 Food Delivery Intelligence Dashboard")

st.markdown(
    """
Welcome to the **Food Delivery Intelligence Platform** — an end-to-end demo that
combines interactive data exploration, real-time deep-learning inference, and
model transparency in a single Streamlit app.

### What you can do here

- **📊 Data Explorer** — Upload a delivery CSV, view summary business metrics,
  and explore interactive Plotly charts of order volume and delivery-time
  distribution.
- **🤖 Demand Predictor** — Enter the hour of day, day of week, and temperature
  to get a live prediction of expected order demand (Low / Medium / High) from
  the trained Keras ANN, along with a confidence breakdown.
- **🧠 Model Info** — Inspect the model's architecture (layers, output shapes,
  parameter counts) and review its training accuracy / loss history.

Use the **sidebar** on the left to navigate between pages.
    """
)

st.info(
    "A sample CSV (`sample_delivery_data.csv`) is included in this folder — "
    "you can upload it directly on the Data Explorer page to try the app."
)

col1, col2, col3 = st.columns(3)
col1.metric("Pages", "4")
col2.metric("Model Type", "Keras ANN")
col3.metric("Framework", "Streamlit + Plotly")
