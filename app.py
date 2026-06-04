import streamlit as st

st.set_page_config(
    page_title="Agriculture Dashboard",
    page_icon="🌾",
    layout="wide"
)

with open("assets/custom.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🌾 Indian Agriculture Analytics Dashboard")

st.markdown("""
Welcome to Agriculture Analytics Dashboard.

Use the navigation panel on the left.
""")
