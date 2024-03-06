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
        return cur.fetchall()
    conn.close()
