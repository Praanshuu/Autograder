
import os
import psycopg2
from urllib.parse import urlparse

# Read .env manually to avoid dependency issues
with open('backend/.env', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('DATABASE_URL='):
            db_url = line.strip().split('=', 1)[1]
            break

result = urlparse(db_url)
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname

print(f"Connecting to {hostname} aka {database}...")

conn = psycopg2.connect(
    dbname=database,
    user=username,
    password=password,
    host=hostname,
    sslmode='require'
)

conn.autocommit = True
cur = conn.cursor()

print("Dropping public schema...")
cur.execute("DROP SCHEMA public CASCADE;")
print("Recreating public schema...")
cur.execute("CREATE SCHEMA public;")
print("Granting permissions...")
cur.execute("GRANT ALL ON SCHEMA public TO public;")
cur.execute("GRANT ALL ON SCHEMA public TO neondb_owner;") 

print("Done! Database is empty.")
conn.close()
