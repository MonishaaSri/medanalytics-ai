Here's the updated `README.md` with API setup change:

Open your `README.md` → replace the API Key Setup section with this:

```markdown
## 🔑 API Key Setup

1. Create a `.env` file in the main project folder
2. Add this line:
```
ANTHROPIC_API_KEY=your_api_key_here
```
3. Get your API key from `console.anthropic.com`
4. The following tabs require API credits:
   - 🔍 SQL Generator
   - 📊 Insight Narrator
   - 🧬 Clinical Trends (AI summary only)
5. These tabs work WITHOUT API key:
   - 🧹 Data Cleaner
   - 🏥 KPI Dashboard
   - 🧬 Clinical Trends (charts only)
```

---

Or just **replace the entire README** with this full updated version:

```markdown
# 🏥 MedAnalytics AI

An AI-powered healthcare analytics platform built with Python, Streamlit, and Claude API.

## 🚀 Run Locally
```bash
streamlit run app.py
```

## 📊 Modules

| Module | Description | Needs API |
|--------|-------------|-----------|
| 🧹 Data Cleaner | Auto-cleans healthcare CSV data | ❌ No |
| 🏥 KPI Dashboard | Visual KPI reporting and charts | ❌ No |
| 🔍 SQL Generator | Natural language → Pandas query | ✅ Yes |
| 📊 Insight Narrator | AI executive business summaries | ✅ Yes |
| 🧬 Clinical Trends | Disease patterns + AI report | ✅ Yes |

## 🗂️ Dataset
- `healthcare_dataset.csv` — 55,500 patient records
- `Disease_symptom_and_patient_profile_dataset.csv` — 349 disease profiles

## 🛠️ Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- Claude API (Anthropic)

## 📁 Project Structure
```
medanalytics-ai/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── data/
│   ├── healthcare_dataset.csv
│   └── Disease_symptom_and_patient_profile_dataset.csv
├── tabs/
│   ├── data_cleaner.py
│   ├── kpi_dashboard.py
│   ├── sql_generator.py
│   ├── insight_narrator.py
│   └── clinical_trends.py
├── prompts/
│   ├── kpi_prompt.md
│   ├── sql_prompt.md
│   ├── insight_prompt.md
│   └── cleaner_prompt.md
└── outputs/
```

## ⚙️ Installation

```bash
git clone https://github.com/MonishaaSri/medanalytics-ai.git
cd medanalytics-ai
pip install -r requirements.txt
streamlit run app.py
```

## 🔑 API Key Setup
1. Create `.env` file in main folder
2. Add:
```
ANTHROPIC_API_KEY=your_api_key_here
```
3. Get API key from `console.anthropic.com`

## 👩‍💻 Built By
Monishaa Sri — Biomedical Engineering + Data Analytics
- GitHub: [MonishaaSri](https://github.com/MonishaaSri)
- LinkedIn: [Monishaa Sri](https://linkedin.com/in/monishaasri)

## 📌 Use Cases
- Healthcare KPI reporting automation
- Natural language data querying
- Executive insight generation
- Clinical research trend analysis
- Data quality improvement
