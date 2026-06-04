import streamlit as st

from utils.data_loader import load_data
from utils.insights import top_state

df = load_data()

state,value = top_state(
    df,
    "RICE PRODUCTION (1000 tons)"
)

st.title("🤖 AI Insights")

st.success(
    f"""
    Top Rice Producing State:
    {state}

    Production:
    {round(value,2)}
    thousand tons
    """
)
