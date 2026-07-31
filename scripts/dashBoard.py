import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
df = pd.read_csv(r"data/raw/SampleSuperstore.csv")

st.title("📊 Super Store Dashboard")

# --- Sidebar filters ---
st.sidebar.header("Filter")
region = st.sidebar.multiselect("Region", df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Category", df["Category"].unique(), default=df["Category"].unique())
segment = st.sidebar.multiselect("Segment", df["Segment"].unique(), default=df["Segment"].unique())

df_filtered = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Segment"].isin(segment))
]

# --- KPI cards ---
col1, col2, col3, col4 = st.columns(4)
total_sales = df_filtered["Sales"].sum()
total_profit = df_filtered["Profit"].sum()
total_qty = df_filtered["Quantity"].sum()
margin = (total_profit / total_sales * 100) if total_sales != 0 else 0

col1.metric("Sales", f"${total_sales:,.0f}")
col2.metric("Profit", f"${total_profit:,.0f}")
col3.metric("Quantity", f"{total_qty:,.0f}")
col4.metric("Profit Margin", f"{margin:.1f}%")

st.divider()

# --- Row 1: Sales by Category & Profit by Region ---
c1, c2 = st.columns(2)

with c1:
    sales_by_cat = df_filtered.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=True).reset_index()
    fig1 = px.bar(sales_by_cat, x="Sales", y="Sub-Category", orientation="h",
                  title="Doanh thu theo Sub-Category")
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    profit_by_region = df_filtered.groupby("Region")["Profit"].sum().reset_index()
    fig2 = px.bar(profit_by_region, x="Region", y="Profit", title="Lợi nhuận theo Region",
                  color="Profit", color_continuous_scale="RdYlGn")
    st.plotly_chart(fig2, use_container_width=True)

# --- Row 2: Segment share & Discount vs Profit ---
c3, c4 = st.columns(2)

with c3:
    seg_sales = df_filtered.groupby("Segment")["Sales"].sum().reset_index()
    fig3 = px.pie(seg_sales, names="Segment", values="Sales", title="Tỷ trọng Sales theo Segment", hole=0.4)
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    fig4 = px.scatter(df_filtered, x="Discount", y="Profit", color="Category",
                       title="Discount vs Profit", opacity=0.6)
    st.plotly_chart(fig4, use_container_width=True)

# --- Table: Top States ---
st.subheader("Top 10 State theo Sales")
top_states = df_filtered.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10).reset_index()
st.dataframe(top_states, use_container_width=True)