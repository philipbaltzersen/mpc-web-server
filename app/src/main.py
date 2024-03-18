import uuid

import psycopg2
from fastapi import Depends, FastAPI, HTTPException

from .connect import get_conn
from .models import Analysis

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/analyses/")
def add_analysis(analysis: Analysis, conn = Depends(get_conn)) -> Analysis:
    if analysis.id is None:
        analysis.id = str(uuid.uuid4())
    
    query = "INSERT INTO analyses (id, owners, file_names, statistical_method) VALUES (%s, %s, %s, %s);"
    
    with conn.cursor() as cur:
        cur.execute(query, (analysis.id, analysis.owners, analysis.file_names, analysis.statistical_method.value))
        conn.commit()
        
    return analysis


@app.get("/analyses/{analysis_id}")
def get_analysis(analysis_id: str, conn = Depends(get_conn)) -> Analysis:
    with conn.cursor() as cur:
        try:
            cur.execute(f"SELECT * FROM analyses WHERE id = '{analysis_id}';")
        except psycopg2.errors.InvalidTextRepresentation:
            raise HTTPException(status_code=400, detail="Invalid UUID format")
        result = cur.fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    return Analysis(
        id=result[0],
        owners=result[1],
        file_names=result[2],
        statistical_method=result[3],
        method_arguments=result[4],
    )
