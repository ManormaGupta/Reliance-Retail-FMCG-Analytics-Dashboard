import os
import pandas as pd
from sqlalchemy import create_engine, text

csv_file = None
for file in os.listdir('.'):
    if file.endswith('.csv'):
        csv_file = file
        break

print(" Loading file...")
df = pd.read_csv(csv_file)
print(" File loaded successfully")

engine = create_engine("mysql+pymysql://root:vaishumanu@localhost/")

with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS reliance_retail_db;"))
    conn.commit()
    print("Database ready")

engine = create_engine("mysql+pymysql://root:vaishumanu@localhost/reliance_retail_db")

print(" Sending data to MySQL... Please wait...")
df.to_sql(name='sales_data', con=engine, if_exists='replace', index=False)

print(" Done! Success.")