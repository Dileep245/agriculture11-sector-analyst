import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

state_prod = (
    df.groupby("State Name")
    ["RICE PRODUCTION (1000 tons)"]
    .sum()
    .reset_index()
)

fig = px.treemap(
    state_prod,
    path=["State Name"],
    values="RICE PRODUCTION (1000 tons)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
