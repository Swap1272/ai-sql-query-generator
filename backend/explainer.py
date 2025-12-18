from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def explain_sql(sql):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": f"Explain this SQL query in simple English:\n{sql}"}
        ]
    )
    return response.choices[0].message.content.strip()
