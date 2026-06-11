import streamlit as st
import pandas as pd
import anthropic
import plotly.express as px
from dotenv import load_dotenv
import os

load_dotenv()

def show():
    st.title("🔍 SQL Query Generator")
    st.write("Type a question in plain English → Claude converts it to SQL → runs it → shows results.")

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        api_key = st.text_input("Enter your Anthropic API Key", type="password")

    uploaded = st.file_uploader("Upload healthcare_dataset.csv", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        df['Name'] = df['Name'].str.title()
        df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')

        st.subheader("📋 Dataset Schema")
        schema = pd.DataFrame({
            'Column': df.columns,
            'Type': df.dtypes.values,
            'Sample': [df[col].iloc[0] for col in df.columns]
        })
        st.dataframe(schema)

        st.subheader("💬 Ask a Question")
        examples = [
            "Show top 10 hospitals by total revenue",
            "Count patients by medical condition",
            "Show average billing amount by admission type",
            "Count male vs female patients",
            "Show top 5 most prescribed medications"
        ]
        st.write("**Example questions:**")
        for ex in examples:
            st.write(f"• {ex}")

        question = st.text_input("Your question:", placeholder="Show top 10 hospitals by revenue")

        if st.button("Generate SQL & Run") and question and api_key:
            with st.spinner("Claude is generating SQL..."):

                schema_text = "\n".join([f"- {col} ({dtype})" for col, dtype in zip(df.columns, df.dtypes)])

                client = anthropic.Anthropic(api_key=api_key)
                message = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1000,
                    messages=[
                        {
                            "role": "user",
                            "content": f"""You are a SQL expert. Convert this question to a pandas query.

Dataset columns:
{schema_text}

Question: {question}

Return ONLY a valid pandas code that:
1. Uses variable name 'df'
2. Stores result in variable 'result'
3. No explanations, only code
4. Maximum 5 lines of code"""
                        }
                    ]
                )

                code = message.content[0].text.strip()
                code = code.replace("```python", "").replace("```", "").strip()

                st.subheader("📝 Generated Code")
                st.code(code, language="python")

                try:
                    local_vars = {"df": df, "pd": pd}
                    exec(code, local_vars)
                    result = local_vars.get("result", None)

                    if result is not None:
                        st.subheader("📊 Query Results")
                        st.dataframe(result)

                        if isinstance(result, pd.DataFrame) and result.shape[1] >= 2:
                            cols = result.columns.tolist()
                            fig = px.bar(result, x=cols[0], y=cols[1],
                                        title=f"Chart: {question}")
                            st.plotly_chart(fig, use_container_width=True)
                except Exception as e:
                    st.error(f"Error running query: {e}")