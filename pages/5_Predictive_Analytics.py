import streamlit as st
import pandas as pd

from sklearn.linear_model import LinearRegression

from utils.data_loader import load_data

df = load_data()

trend = (
    df.groupby("Year")
    ["RICE PRODUCTION (1000 tons)"]
    .sum()
    .reset_index()
)

model = LinearRegression()

model.fit(
    trend[["Year"]],
    trend[
        "RICE PRODUCTION (1000 tons)"
    ]
)

future = pd.DataFrame({
    "Year":[
        2025,
        2026,
        2027,
        2028,
        2029,
        2030
    ]
})

future["Prediction"] = model.predict(
    future[["Year"]]
)

st.dataframe(future)
