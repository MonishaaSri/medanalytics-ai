import streamlit as st
from tabs import data_cleaner, kpi_dashboard, sql_generator, insight_narrator, clinical_trends

st.set_page_config(
    page_title="MedAnalytics AI",
    page_icon="🏥",
    layout="wide"
)

# Sidebar
st.sidebar.image("https://img.icons8.com/color/96/hospital.png", width=80)
st.sidebar.title("🏥 MedAnalytics AI")
st.sidebar.markdown("AI-Powered Healthcare Analytics Platform")
st.sidebar.markdown("---")

tabs = {
    "🧹 Data Cleaner": data_cleaner,
    "🏥 KPI Dashboard": kpi_dashboard,
    "🔍 SQL Generator": sql_generator,
    "📊 Insight Narrator": insight_narrator,
    "🧬 Clinical Trends": clinical_trends
}

selected = st.sidebar.radio("Select Module", list(tabs.keys()))
st.sidebar.markdown("---")
st.sidebar.markdown("Built with Claude API + Streamlit")
st.sidebar.markdown("By Monishaa Sri")

# Load selected tab
tabs[selected].show()