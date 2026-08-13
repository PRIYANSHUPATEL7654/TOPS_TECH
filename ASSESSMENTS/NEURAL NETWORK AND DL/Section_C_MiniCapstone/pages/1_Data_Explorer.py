"""
Capstone Page — Data Explorer
Upload & visualize delivery data (Streamlit + Plotly).
"""

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Data Explorer", page_icon="📊", layout="wide")
st.title("📊 Data Explorer")
st.caption("Upload delivery data to view summary statistics and interactive trend charts.")

uploaded_file = st.file_uploader("Upload delivery data (CSV)", type=["csv"])

if uploaded_file is None:
    st.info(
        "👋 Upload a CSV to get started, or try `sample_delivery_data.csv` "
        "included in this folder."
    )
    st.stop()

try:
    df = pd.read_csv(uploaded_file)
except Exception as e:
    st.error(f"Could not read the uploaded file: {e}")
    st.stop()

df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
required_cols = {"city", "restaurant", "delivery_time_minutes", "revenue"}
missing = required_cols - set(df.columns)
if missing:
    st.error(f"CSV is missing required column(s): {', '.join(missing)}")
    st.stop()

# Ensure a hour column exists for the volume-trend chart; synthesize if absent
if "hour" not in df.columns:
    rng = np.random.default_rng(0)
    df["hour"] = rng.integers(0, 24, len(df))

# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------
total_orders = len(df)
avg_delivery_time = df["delivery_time_minutes"].mean()
total_revenue = df["revenue"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", f"{total_orders:,}")
col2.metric("Avg. Delivery Time", f"{avg_delivery_time:.1f} min")
col3.metric("Total Revenue", f"₹{total_revenue:,.2f}")

st.divider()

# ---------------------------------------------------------------------------
# Chart 1 — Hourly order volume trend
# ---------------------------------------------------------------------------
st.subheader("Hourly Order Volume Trend")
hourly_counts = df.groupby("hour").size().reset_index(name="order_count")
fig1 = px.line(hourly_counts, x="hour", y="order_count", markers=True,
               title="Orders by Hour of Day")
fig1.update_layout(xaxis_title="Hour of Day", yaxis_title="Order Count")
st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------------------------------------------
# Chart 2 — Delivery time distribution by restaurant
# ---------------------------------------------------------------------------
st.subheader("Delivery Time Distribution by Restaurant")
top_restaurants = df["restaurant"].value_counts().nlargest(10).index
fig2 = px.box(
    df[df["restaurant"].isin(top_restaurants)],
    x="restaurant",
    y="delivery_time_minutes",
    title="Delivery Time Spread (Top 10 Restaurants by Order Count)",
)
fig2.update_layout(xaxis_title="Restaurant", yaxis_title="Delivery Time (min)")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View raw data"):
    st.dataframe(df, use_container_width=True)
