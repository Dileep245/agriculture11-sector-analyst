import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("📊 Overview Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "States",
    df["State Name"].nunique()
)

col2.metric(
    "Districts",
    df["Dist Name"].nunique()
)

col3.metric(
    "Years",
    df["Year"].nunique()
)

col4.metric(
    "Records",
    len(df)
)

trend = (
    df.groupby("Year")
    ["RICE PRODUCTION (1000 tons)"]
    .sum()
    .reset_index()
)

fig = px.line(
    trend,
    x="Year",
    y="RICE PRODUCTION (1000 tons)",
    title="Rice Production Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
