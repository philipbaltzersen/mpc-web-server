import pandas as pd
import scipy.stats as sp
from fastapi import FastAPI

from .connect import connect

app = FastAPI()

conn = connect()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/data/{owner}")
def read_data(owner: str):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM data WHERE owner = '{owner}';")
        result = cur.fetchall()
    conn.close()
    return result

@app.get("/analyze")
def analyze_data():
    with conn.cursor() as cur:
        cur.execute("SELECT data->'before', data->'after' FROM data;")
        df = pd.DataFrame(cur.fetchall(), columns=["before", "after"])
    
    statistic, p_value = sp.ttest_ind(df["before"], df["after"])
    conn.close()
    return {"statistic": statistic, "p_value": p_value}
