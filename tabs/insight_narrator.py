import streamlit as st
import pandas as pd
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

def show():
    st.title("📊 Insight Narrator")
    st.write("Upload data → Claude generates executive business summary automatically.")

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        api_key = st.text_input("Enter your Anthropic API Key", type="password")

    uploaded = st.file_uploader("Upload healthcare_dataset.csv", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        df['Billing Amount'] = pd.to_numeric(df['Billing Amount'], errors='coerce')
        df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')

        st.subheader("📋 Data Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Patients", df.shape[0])
        col2.metric("Total Revenue", f"${df['Billing Amount'].sum():,.0f}")
        col3.metric("Avg Billing", f"${df['Billing Amount'].mean():,.0f}")

        top_condition = df.groupby('Medical Condition')['Billing Amount'].mean().idxmax()
        top_hospital = df['Hospital'].value_counts().idxmax()
        top_admission = df['Admission Type'].value_counts().idxmax()
        top_insurance = df['Insurance Provider'].value_counts().idxmax()
        avg_billing = df['Billing Amount'].mean()
        total_patients = df.shape[0]

        kpi_summary = f"""
        Total Patients: {total_patients}
        Total Revenue: ${df['Billing Amount'].sum():,.0f}
        Average Billing Amount: ${avg_billing:,.0f}
        Highest Billing Medical Condition: {top_condition}
        Most Common Admission Type: {top_admission}
        Top Hospital by Patient Count: {top_hospital}
        Most Used Insurance Provider: {top_insurance}
        Male Patients: {df[df['Gender']=='Male'].shape[0]}
        Female Patients: {df[df['Gender']=='Female'].shape[0]}
        Most Prescribed Medication: {df['Medication'].value_counts().idxmax()}
        """

        st.subheader("📈 KPI Summary")
        st.text(kpi_summary)

        if st.button("🤖 Generate Executive Insights") and api_key:
            with st.spinner("Claude is writing insights..."):

                client = anthropic.Anthropic(api_key=api_key)
                message = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1000,
                    messages=[
                        {
                            "role": "user",
                            "content": f"""You are a healthcare business analyst.
Based on this KPI summary, write a professional executive report in 5-6 paragraphs.

{kpi_summary}

Include:
- Overall performance summary
- Revenue insights
- Patient demographics
- Admission trends
- Key recommendations

Write in a professional business tone."""
                        }
                    ]
                )

                insight = message.content[0].text.strip()

                st.subheader("📝 Executive Insights Report")
                st.write(insight)

                st.download_button(
                    label="⬇️ Download Report",
                    data=insight,
                    file_name="executive_insights.txt",
                    mime="text/plain"
                )