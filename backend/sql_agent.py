from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE

client = OpenAI(api_key=OPENAI_API_KEY) 
SQL_PROMPT = """
You are an expert SQL developer.        
Database: {db_type}
Schema:
{schema}
Rules:
- Use only SELECT queries
- Do NOT use DELETE, UPDATE, DROP, INSERT, TRUNCATE
- Return only SQL       

User question:
{question}
""" 
def generate_sql(question, schema, db_type):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "Generate safe SQL only."},
            {"role": "user", "content": SQL_PROMPT.format(
                question=question,
                schema=schema,
                db_type=db_type
            )}
        ],
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE
    )
    return response.choices[0].message.content.strip()  
print("API KEY FOUND:", OPENAI_API_KEY)





