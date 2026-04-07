import os
import sqlite3

try:
    script_path = r'd:\New folder (3)\job_market_dashboard\notebooks\Model_Training.py'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(script_path)))
    db_path = os.path.join(BASE_DIR, 'data', 'job_market.db')
    
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"db_path: {db_path}")
    print(f"Exists: {os.path.exists(db_path)}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables: {tables}")
    
    if ('cleaned_jobs',) in tables:
        count = conn.execute("SELECT COUNT(*) FROM cleaned_jobs WHERE salary_disclosed = 1").fetchone()[0]
        print(f"Jobs with salary: {count}")
    
except Exception as e:
    print(f"Error: {e}")
