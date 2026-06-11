import streamlit as st
import pandas as pd
import plotly.express as px
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

def show():
    st.title("🧬 Clinical Trends Analyzer")
    st.write("Analyze disease patterns, symptoms and patient outcomes.")

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        api_key = st.text_input("Enter your Anthropic API Key", type="password")

    uploaded = st.file_uploader("Upload Disease_symptom_and_patient_profile_dataset.csv", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)

        st.subheader("📋 Dataset Preview")
        st.dataframe(df.head(10))

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records", df.shape[0])
        col2.metric("Total Diseases", df['Disease'].nunique())
        col3.metric("Positive Outcomes", df[df['Outcome Variable']=='Positive'].shape[0])

        st.subheader("🦠 Top Diseases by Count")
        disease_count = df['Disease'].value_counts().head(10).reset_index()
        disease_count.columns = ['Disease', 'Count']
        fig1 = px.bar(disease_count, x='Disease', y='Count',
                      color='Disease', title="Top 10 Diseases")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("🌡️ Symptom Frequency")
        symptoms = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']
        symptom_counts = {}
        for s in symptoms:
            if s in df.columns:
                symptom_counts[s] = df[df[s]=='Yes'].shape[0]
        sym_df = pd.DataFrame(list(symptom_counts.items()), columns=['Symptom', 'Count'])
        fig2 = px.bar(sym_df, x='Symptom', y='Count',
                      color='Symptom', title="Symptom Frequency")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("✅ Outcome by Disease")
        outcome = df.groupby(['Disease', 'Outcome Variable']).size().reset_index(name='Count')
        fig3 = px.bar(outcome, x='Disease', y='Count',
                      color='Outcome Variable', barmode='group',
                      title="Positive vs Negative Outcomes by Disease")
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("👥 Gender Distribution")
        gender = df['Gender'].value_counts().reset_index()
        gender.columns = ['Gender', 'Count']
        fig4 = px.pie(gender, names='Gender', values='Count',
                      title="Gender Distribution")
        st.plotly_chart(fig4, use_container_width=True)

        st.subheader("🩸 Blood Pressure Distribution")
        bp = df['Blood Pressure'].value_counts().reset_index()
        bp.columns = ['Blood Pressure', 'Count']
        fig5 = px.bar(bp, x='Blood Pressure', y='Count',
                      color='Blood Pressure', title="Blood Pressure Levels")
        st.plotly_chart(fig5, use_container_width=True)

        if st.button("🤖 Generate Clinical Research Summary") and api_key:
            with st.spinner("Claude is analyzing clinical trends..."):

                summary = f"""
                Total Records: {df.shape[0]}
                Total Unique Diseases: {df['Disease'].nunique()}
                Most Common Disease: {df['Disease'].value_counts().idxmax()}
                Positive Outcomes: {df[df['Outcome Variable']=='Positive'].shape[0]}
                Negative Outcomes: {df[df['Outcome Variable']=='Negative'].shape[0]}
                Most Common Symptom: {max(symptom_counts, key=symptom_counts.get)}
                Avg Age: {df['Age'].mean():.1f}
                Most Common Blood Pressure: {df['Blood Pressure'].value_counts().idxmax()}
                Most Common Cholesterol: {df['Cholesterol Level'].value_counts().idxmax()}
                """

                client = anthropic.Anthropic(api_key=api_key)
                message = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1000,
                    messages=[
                        {
                            "role": "user",
                            "content": f"""You are a clinical research analyst.
Based on this disease and symptom dataset summary, write a professional clinical research report.

{summary}

Include:
- Disease prevalence findings
- Symptom pattern analysis
- Patient demographic insights
- Outcome analysis
- Clinical recommendations

Write in a professional medical research tone."""
                        }
                    ]
                )

                report = message.content[0].text.strip()
                st.subheader("📝 Clinical Research Report")
                st.write(report)

                st.download_button(
                    label="⬇️ Download Clinical Report",
                    data=report,
                    file_name="clinical_research_report.txt",
                    mime="text/plain"
                )