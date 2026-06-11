**Create `README.md`**

Open Notepad → copy paste this:

```markdown
# 🏥 MedAnalytics AI

An AI-powered healthcare analytics platform built with Python, Streamlit, and Claude API.

## 🚀 Live Demo
Run locally with: `streamlit run app.py`

## 📊 Modules

| Module | Description |
|--------|-------------|
| 🧹 Data Cleaner | Auto-cleans healthcare CSV data — fixes names, dates, nulls, duplicates |
| 🏥 KPI Dashboard | Visual KPI reporting — revenue, admissions, billing trends |
| 🔍 SQL Generator | Natural language → Pandas query → results + charts |
| 📊 Insight Narrator | AI-generated executive business summaries |
| 🧬 Clinical Trends | Disease pattern analysis, symptom frequency, outcome insights |

## 🗂️ Dataset
- `healthcare_dataset.csv` — 55,500 patient records
- `Disease_symptom_and_patient_profile_dataset.csv` — 349 disease profiles

## 🛠️ Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- Claude API (Anthropic)
- SQL / Pandas Query Engine

## 📁 Project Structure
```
medanalytics-ai/
├── app.py
├── requirements.txt
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
- Get your API key from `console.anthropic.com`
- Paste it in the app when prompted

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
```

Save it:
- File name: `README.md`
- Save as type: **All Files**
- Save in **main `medanalytics-ai` folder**

---

Your folder should now look like:
```
medanalytics-ai/
├── data/
├── outputs/
├── prompts/
├── tabs/
├── app.py
├── requirements.txt
├── apikey.txt
└── README.md ✅
```

**Tell me when saved → we'll push to GitHub next.**
