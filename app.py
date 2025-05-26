import streamlit as st
from openai import OpenAI
from streamlit_mermaid import st_mermaid

st.set_page_config(
    page_title="ETLGenie — AI ETL Consultant",
    page_icon="🛰️",
    layout="centered"
)

st.markdown("""
    <style>
    /* Fix font using fallback Inter/Segoe UI and boost contrast */

    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif;
        background: linear-gradient(145deg, #e6e9f0, #eef1f5);
        color: #111 !important;
    }

    .stApp {
        background: url('https://www.transparenttextures.com/patterns/cubes.png');
        background-size: contain;
    }

    .main-container {
        max-width: 1900px;
        margin: 40px auto;
        background: white;
        padding: 2rem 6rem;
        border-radius: 200px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
    }

    h1, h2, h3, .stMarkdown h1, .stMarkdown h2 {
        color: #111 !important;
    }

    .stTextInput > div > div > input, .stTextArea textarea, .stSelectbox > div > div {
        background-color: #ffffff;
        color: #111;
        border-radius: 12px;
        border: 1px solid #ccc;
        font-size: 16px;
        padding: 10px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.04);
    }

    .stButton > button {
        background: linear-gradient(to right, #6a11cb, #2575fc);
        color: white;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #5f2c82, #49a09d);
        transform: scale(1.03);
    }

    .stMarkdown code {
        background: #f5f5f7;
        padding: 5px 8px;
        border-radius: 6px;
        font-size: 14px;
        color: #c7254e;
    }

    footer {
    visibility: hidden;
    }

    /* 👇 Add this at the bottom */
    [data-testid="stMarkdownContainer"] * {
        color: #111111 !important;
    }

    div[data-testid="stCaptionContainer"] {
        color: #555555 !important;
        font-weight: 500;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


st.title("🛰️ ETLGenie — Auto ETL Workflow Generator")
st.caption("Describe your pipeline use case and get back an AI-generated ETL plan.")

use_case = st.text_area("📌 Describe your ETL need (e.g., 'Extract Shopify orders and load to BigQuery daily')")

output_format = st.selectbox("🧠 Output Type", ["ETL Steps", "Airflow YAML", "DAG Diagram (Mermaid)"])

if st.button("✨ Generate ETL Flow"):
    with st.spinner("Thinking like a data engineer..."):
        prompt = f"""
        You are a senior data engineer and solutions consultant. Based on the business use case below, generate an **in-depth ETL project plan** that includes the following clearly marked sections using markdown headers (##):

        ## Extract  
        Describe source, connection method, tool (Airbyte/Fivetran), and frequency.

        ## Transform  
        Describe logic, tool (dbt/Spark), and model examples.

        ## Load  
        Describe destination (BigQuery, Snowflake), write strategy, and partitioning.

        ## Visualize  
        Describe dashboard ideas, metrics, and BI tool setup.

        ## Tools  
        Give tool recommendations per stage with 1-line descriptions and official links.

        ## Timeline  
        Break the project into weekly phases: setup → dev → QA → deploy.

        ## Team  
        Suggest what kind of engineers are needed, with roles and counts.

        ## Industry  
        Explain how the same ETL applies to 2–3 industries (e.g., finance, e-commerce).

        ## DAG Diagram  
        End with a mermaid diagram of the workflow.

        Use Case: {use_case}
        """


        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a senior data engineer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=800
        )

        result = response.choices[0].message.content

        import re

        # Extract Mermaid diagram
        dag_match = re.search(r"```mermaid(.*?)```", result, re.DOTALL)
        mermaid_diagram = dag_match.group(1).strip() if dag_match else ""

        # Parse result into sections
        sections = {
            "extract": "",
            "transform": "",
            "load": "",
            "visualize": "",
            "tools": "",
            "timeline": "",
            "team": "",
            "industry": "",
        }

        for key in sections:
            match = re.search(rf"(?i)##?\s*{key}", result)
            if match:
                start = match.start()
                next_match = re.search(rf"(?i)##?\s*(extract|transform|load|visualize|tools|timeline|team|industry|dag)", result[start + 5:])
                end = next_match.start() + start + 5 if next_match else len(result)
                sections[key] = result[start:end].strip()

        # 🧾 Sectioned Output
        st.markdown("### 🧾 Full ETL Plan")

        with st.expander("📜 Raw Output from OpenAI"):
            st.code(result, language="markdown")

        if sections["extract"]:
            st.markdown("## 🧪 Extract")
            st.markdown(sections["extract"])

        if sections["transform"]:
            st.markdown("## 🔄 Transform")
            st.markdown(sections["transform"])

        if sections["load"]:
            st.markdown("## 📥 Load")
            st.markdown(sections["load"])

        if sections["visualize"]:
            st.markdown("## 📊 Visualize")
            st.markdown(sections["visualize"])

        if sections["tools"]:
            st.markdown("## 🧰 Tools & Resources")
            st.markdown(sections["tools"])

        if sections["timeline"]:
            st.markdown("## ⏳ Timeline")
            st.markdown(sections["timeline"])

        if sections["team"]:
            st.markdown("## 👥 Team & Roles")
            st.markdown(sections["team"])

        if sections["industry"]:
            st.markdown("## 🏭 Industry Use Cases")
            st.markdown(sections["industry"])

        # DAG Preview
        if mermaid_diagram:
            st.markdown("## 🧭 DAG Diagram")
            st_mermaid(mermaid_diagram)

st.markdown("---")
st.markdown("✅ Built with ❤️ by [@jugalsheth](https://github.com/jugalsheth) | Powered by OpenAI + Streamlit")
