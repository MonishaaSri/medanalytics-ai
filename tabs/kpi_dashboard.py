import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.title("🏥 KPI Dashboard")
    st.write("Healthcare KPI analysis from patient records.")

    uploaded = st.file_uploader("Upload healthcare_dataset.csv", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)

        # Clean names
        df['Name'] = df['Name'].str.title()
        df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')

        st.subheader("📊 Key Metrics")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Patients", df.shape[0])
        col2.metric("Total Revenue", f"${df['Billing Amount'].sum():,.0f}")
        col3.metric("Avg Billing", f"${df['Billing Amount'].mean():,.0f}")
        col4.metric("Hospitals", df['Hospital'].nunique())

        st.subheader("💰 Avg Billing by Medical Condition")
        billing = df.groupby('Medical Condition')['Billing Amount'].mean().reset_index()
        fig1 = px.bar(billing, x='Medical Condition', y='Billing Amount',
                      color='Medical Condition', title="Avg Billing by Condition")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("🏨 Admission Type Breakdown")
        admission = df['Admission Type'].value_counts().reset_index()
        admission.columns = ['Admission Type', 'Count']
        fig2 = px.pie(admission, names='Admission Type', values='Count',
                      title="Admission Type Distribution")
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("🏆 Top 10 Hospitals by Patient Count")
        hospitals = df['Hospital'].value_counts().head(10).reset_index()
        hospitals.columns = ['Hospital', 'Count']
        fig3 = px.bar(hospitals, x='Count', y='Hospital', orientation='h',
                      title="Top 10 Hospitals", color='Count')
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("📈 Monthly Admissions Trend")
        df['Month'] = df['Date of Admission'].dt.to_period('M').astype(str)
        monthly = df.groupby('Month').size().reset_index(name='Admissions')
        fig4 = px.line(monthly, x='Month', y='Admissions',
                       title="Monthly Admissions Trend")
        st.plotly_chart(fig4, use_container_width=True)