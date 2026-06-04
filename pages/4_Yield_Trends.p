import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

yield_data = (
    df.groupby("Year")
    ["RICE YIELD (Kg per ha)"]
    .mean()
    .reset_index()
)

fig = px.line(
    yield_data,
    x="Year",
    y="RICE YIELD (Kg per ha)",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)
