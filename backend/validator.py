FORBIDDEN_KEYWORDS = [
    "delete", "update", "drop", "truncate", "insert", "alter"
]

def validate_sql(sql: str):
    sql_lower = sql.lower()
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_lower:
            raise ValueError("Unsafe SQL detected")
    return True
