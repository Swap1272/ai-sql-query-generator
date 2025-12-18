import streamlit as st
import requests

st.set_page_config(page_title="AI SQL Query Generator")

st.title("AI SQL Query Generator")

question = st.text_input("Enter your question")
db_type = st.selectbox("Database Type", ["MySQL", "PostgreSQL"])
schema = st.text_area("Paste your DB schema")

if st.button("Generate SQL"):
    response = requests.post(
        "http://localhost:8000/generate",
        json={
            "question": question,
            "schema": schema,
            "db_type": db_type
        }
    )
    data = response.json()
    st.subheader("Generated SQL")
    st.code(data["sql"])

    st.subheader("Explanation")
    st.write(data["explanation"])
