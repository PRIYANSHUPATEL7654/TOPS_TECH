"""
Task 1 — Delivery Summary Dashboard
Section B, Module 8 (Streamlit)

Run with:  streamlit run app.py

Expected CSV columns (case-insensitive, flexible):
    city, restaurant, delivery_time_minutes, revenue
(order count is simply the row count per group)
"""

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Delivery Summary Dashboard", layout="wide")

st.title("🍔 Delivery Summary Dashboard")
st.caption("Upload a food-delivery CSV to explore city-level performance metrics.")

# ---------------------------------------------------------------------------
# Requirement 1 — File uploader with placeholder message
# ---------------------------------------------------------------------------
uploaded_file = st.file_uploader("Upload delivery data (CSV)", type=["csv"])

if uploaded_file is None:
    st.info("👋 Please upload a delivery data CSV file to see the dashboard.")
    st.stop()

df = pd.read_csv(uploaded_file)
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

required_cols = {"city", "restaurant", "delivery_time_minutes", "revenue"}
missing = required_cols - set(df.columns)
if missing:
    st.error(f"The uploaded CSV is missing required column(s): {', '.join(missing)}")
    st.stop()

# ---------------------------------------------------------------------------
# Requirement 3 — Sidebar city filter
# ---------------------------------------------------------------------------
st.sidebar.header("Filters")
cities = sorted(df["city"].dropna().unique().tolist())
selected_city = st.sidebar.selectbox("Select City", cities)

filtered_df = df[df["city"] == selected_city]

# ---------------------------------------------------------------------------
# Requirement 2 — Metric cards (recomputed for the selected city)
# ---------------------------------------------------------------------------
total_orders = len(filtered_df)
avg_delivery_time = filtered_df["delivery_time_minutes"].mean() if total_orders else 0
total_revenue = filtered_df["revenue"].sum() if total_orders else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", f"{total_orders:,}")
col2.metric("Avg. Delivery Time", f"{avg_delivery_time:.1f} min")
col3.metric("Total Revenue", f"₹{total_revenue:,.2f}")

st.divider()

# ---------------------------------------------------------------------------
# Requirement 4 — Bar chart: order count per restaurant for selected city
# ---------------------------------------------------------------------------
st.subheader(f"Orders per Restaurant — {selected_city}")

if total_orders == 0:
    st.warning("No records found for the selected city.")
else:
    orders_per_restaurant = (
        filtered_df.groupby("restaurant").size().sort_values(ascending=False)
    )
    st.bar_chart(orders_per_restaurant)

    with st.expander("View filtered data"):
        st.dataframe(filtered_df, use_container_width=True)
