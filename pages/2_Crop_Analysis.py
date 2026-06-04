import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

crop = st.selectbox(
    "Select Crop",
    [
        "RICE",
        "WHEAT",
        "MAIZE"
    ]
)

production_column = (
    crop +
    " PRODUCTION (1000 tons)"
)

top_states = (
    df.groupby("State Name")
    [production_column]
    .sum()
    .sort_values(ascending=False)
    .head(15)
)

fig = px.bar(
    top_states,
    title=f"Top States for {crop}"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
