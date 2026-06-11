import streamlit as st
import pandas as pd

def show():
    st.title("🧹 Data Cleaner")
    st.write("Upload healthcare data to clean and download.")

    uploaded = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        st.subheader("📋 Raw Data Preview")
        st.dataframe(df.head(10))

        st.subheader("🔍 Data Quality Report")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Rows", df.shape[0])
        col2.metric("Null Values", df.isnull().sum().sum())
        col3.metric("Duplicates", df.duplicated().sum())

        st.subheader("🔧 Cleaning Steps")

        # Fix name casing
        if 'Name' in df.columns:
            df['Name'] = df['Name'].str.title()
            st.write("✅ Fixed name casing")

        # Fix date formats
        for col in ['Date of Admission', 'Discharge Date']:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
                st.write(f"✅ Fixed date format: {col}")

        # Remove duplicates
        before = df.shape[0]
        df = df.drop_duplicates()
        after = df.shape[0]
        st.write(f"✅ Removed {before - after} duplicates")

        # Fill nulls
        df = df.fillna("Unknown")
        st.write("✅ Filled null values with 'Unknown'")

        st.subheader("✨ Cleaned Data Preview")
        st.dataframe(df.head(10))

        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Cleaned CSV",
            data=csv,
            file_name="cleaned_healthcare_data.csv",
            mime="text/csv"
        )