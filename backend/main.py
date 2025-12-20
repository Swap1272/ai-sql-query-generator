from fastapi import FastAPI
from sql_agent import generate_sql
from validator import validate_sql
from explainer import explain_sql

app = FastAPI()

@app.post("/generate")
def generate(query: dict):
    sql = generate_sql(
        query["question"],
        query["schema"],
        query["db_type"]
    )
    validate_sql(sql)
    explanation = explain_sql(sql)
    return {
        "sql": sql,
        "explanation": explanation
    }


    
