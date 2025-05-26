# 🧞‍♂️ ETLGenie — AI-Powered ETL Project Designer & Consultant

ETLGenie is your AI assistant for designing complete ETL pipelines — from natural language input to full project blueprints.  
Get everything from step-by-step ETL plans, tool recommendations, YAML configs, architecture diagrams, team resourcing, and timelines.

---

## ✨ Features

✅ Natural Language → Full ETL Blueprint  
✅ Extract, Transform, Load, Visualize (with best practices)  
✅ Tool suggestions (Airbyte, Fivetran, dbt, Spark, Snowflake, BigQuery, Tableau)  
✅ YAML / SQL Config Templates  
✅ Mermaid DAG diagram generation  
✅ Project Timeline (weekly phases)  
✅ Team & Role allocation suggestions  
✅ Industry-specific variations  
✅ Streamlit-based modern UI (fully responsive)

---

## 🧠 Example Input

> _"Extract Shopify orders and load to BigQuery daily. Provide tools, config, roles, timeline, and DAG."_

## 📤 Example Output

- ✅ ETL breakdown by stage  
- ✅ Tool suggestions (with links)  
- ✅ Config snippets  
- ✅ Mermaid DAG code  
- ✅ Weekly roadmap  
- ✅ Team roles (e.g. 1 data engineer, 1 analytics engineer)  
- ✅ Use-case adaptation across industries

---

## 🖼️ App Preview


![Screenshot 2025-05-26 at 4 45 44 PM](https://github.com/user-attachments/assets/7c6e221d-dbd8-45c3-a4e5-5fb73453d8a1)
![Screenshot 2025-05-26 at 4 46 16 PM](https://github.com/user-attachments/assets/0749eca0-cc5c-4710-9b1a-d06afd24b624)


---


### 1. Clone the Repository

```bash
git clone https://github.com/jugalsheth/etlgenie.git
cd etlgenie

2. Create Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt

3. Add Your OpenAI Key
Create a .streamlit/secrets.toml file in the root directory:

toml
Copy
Edit
OPENAI_API_KEY = "your-openai-key"

4. Run the App
bash
Copy
Edit
streamlit run app.py

🧰 Tech Stack
Layer	Tech Used
UI Framework	Streamlit
LLM Engine	OpenAI GPT-3.5
Diagram	Mermaid.js via streamlit-mermaid
Styling	Custom HTML + CSS

🧪 Output Includes
🔹 ETL Plan with markdown headers
🔹 Mermaid DAG rendered inside app
🔹 Expandable raw OpenAI output
🔹 Modular, extensible layout

🌐 Roadmap (Coming Soon)
 Streamlit Cloud deployment
 Export config as downloadable .yaml / .sql
 Interactive DAG editing
 Lottie AI assistant animation
 API endpoint version

👨‍💻 Author
Built by @jugalsheth
🧠 Data engineer by trade, GenAI tinkerer by night.

💬 Feedback & Contributions
Feel free to open an issue or suggest a feature.
If you found this useful, ⭐️ star the repo or share it!



