import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# PAGE CONFIGURATION
# -------------------------
st.set_page_config(
    page_title="🌾 Indian Agriculture Analytics",
    page_icon="🌾",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.metric-card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

h1,h2,h3 {
    color: #2E7D32;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# TITLE
# -------------------------
st.title("🌾 Indian Agriculture Analytics Dashboard")

st.markdown("""
### Deep Analytics of Indian Agriculture using ICRISAT Dataset

This dashboard provides:

- 📊 Crop Production Analysis
- 📈 Yield Trend Analysis
- 🏆 Top Performing States
- 🌍 Geographic Insights
- 🔮 Production Forecasting
- 🤖 Automated Insights
""")

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/ICRISAT-District-Level-Data.csv")

try:
    df = load_data()

    # -------------------------
    # KPI SECTION
    # -------------------------
    st.subheader("📌 Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "States",
            df["State Name"].nunique()
        )

    with col2:
        st.metric(
            "Districts",
            df["Dist Name"].nunique()
        )

    with col3:
        st.metric(
            "Years",
            df["Year"].nunique()
        )

    with col4:
        st.metric(
            "Records",
            len(df)
        )

    st.divider()

    # -------------------------
    # RICE PRODUCTION TREND
    # -------------------------
    st.subheader("📈 Rice Production Trend")

    rice_col = "RICE PRODUCTION (1000 tons)"

    if rice_col in df.columns:

        trend = (
            df.groupby("Year")[rice_col]
            .sum()
            .reset_index()
        )

        fig = px.line(
            trend,
            x="Year",
            y=rice_col,
            markers=True,
            title="Rice Production Over Time"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -------------------------
    # TOP STATES
    # -------------------------
    st.subheader("🏆 Top Rice Producing States")

    if rice_col in df.columns:

        top_states = (
            df.groupby("State Name")[rice_col]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            top_states,
            x="State Name",
            y=rice_col,
            title="Top 10 Rice Producing States"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -------------------------
    # DATA PREVIEW
    # -------------------------
    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    # -------------------------
    # SUMMARY
    # -------------------------
    st.subheader("🤖 Quick Insights")

    if rice_col in df.columns:

        top_state = (
            df.groupby("State Name")[rice_col]
            .sum()
            .idxmax()
        )

        top_production = (
            df.groupby("State Name")[rice_col]
            .sum()
            .max()
        )

        st.success(
            f"""
            Highest Rice Producing State: **{top_state}**

            Total Production: **{top_production:,.2f} Thousand Tons**
            """
        )

except FileNotFoundError:
    st.error(
        "Dataset not found. Place the CSV file inside the data folder."
    )
