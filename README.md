# 📊 Customer Support Ticket Analytics & AI Report Generator

An automated data pipeline written in Python that ingests raw customer support ticket data, calculates key operational metrics, synthesizes strategic business insights using **Google Gemini API**, and exports executive-ready Word (`.docx`) reports.

## 🚀 Features
- **Data Aggregation (Pandas):** Processes 20,000+ support tickets to calculate daily volume, CSAT scores, channel distribution, top issue categories, and agent ratings.
- **AI Analytics (Google Gemini API):** Leverages `gemini-3.1-flash-lite` to automatically generate executive summaries, key takeaways, and strategic recommendations based on aggregated data.
- **Automated Reporting (`python-docx`):** Formats and exports metrics and AI-generated insights into structured Word documents.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Data Processing:** Pandas
- **AI / LLM:** Google GenAI SDK (`google-genai`)
- **Document Export:** `python-docx`
- **Environment Management:** `python-dotenv`

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ai_analytics_learning.git](https://github.com/YOUR_USERNAME/ai_analytics_learning.git)
   cd ai_analytics_learning