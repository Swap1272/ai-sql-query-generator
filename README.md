**AI SQL Query Generator**
A FastAPI application that generates safe SQL queries from natural language questions using OpenAI models. It also validates queries against unsafe keywords and provides plain‑English explanations of the generated SQL.

🚀 Features
SQL Generation: **Converts user questions into SQL queries.**

Validation: **Blocks unsafe operations (DELETE, UPDATE, DROP, INSERT, TRUNCATE, ALTER).**

Explanation: **Explains SQL queries in simple English.**

REST API: Exposed via FastAPI with /generate endpoint.

Deploy Ready📂 Project Structure
Code
ai-sql-query-generator/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── sql_agent.py
│   ├── validator.py
│   ├── explainer.py
│   ├── config.py
├── requirements.txt
├── Procfile
├── README.md

⚙️ Setup Instructions
1. Clone the repository
bash
git clone https://github.com/your-username/ai-sql-query-generator.git
cd ai-sql-query-generator
2. Create a virtual environment
bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
.\venv\Scripts\activate    # Windows
3. Install dependencies
bash
pip install -r requirements.txt
4. Set environment variables
You must manually set your OpenAI API key before running the app. This project does not include the key for security reasons.

Linux/Mac

bash
export OPENAI_API_KEY="sk-your-secret-key"
export MODEL_NAME="gpt-4o-mini"
export MAX_TOKENS="500"
export TEMPERATURE="0.2"
Windows PowerShell

powershell
$env:OPENAI_API_KEY="sk-your-secret-key"
$env:MODEL_NAME="gpt-4o-mini"
$env:MAX_TOKENS="500"
$env:TEMPERATURE="0.2"
⚠️ Important: Do not commit your API key to GitHub. Each user must set their own key manually.

▶️ Running Locally
bash
uvicorn backend.main:app --reload
Open http://localhost:8000/docs to test the API.

🌐 Deploying on Render
Root Directory: repo root

Build Command:

bash
pip install -r requirements.txt
Start Command:

bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
Add environment variables (OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE) in Render dashboard.

📬 Example Request
POST /generate

json
{
  "question": "Show me all customers from New York",
  "schema": "Table: customers(id, name, city)",
  "db_type": "PostgreSQL"
}
Response:

json
{
  "sql": "SELECT * FROM customers WHERE city = 'New York';",
  "explanation": "This query retrieves all customers who live in New York."
}
🔒 Security Note
**The app only allows SELECT queries.**

Unsafe SQL keywords are blocked by the validator.

**API key must be set manually by each user — never share or commit it.**

