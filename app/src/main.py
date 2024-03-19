import json
import uuid
from typing import Annotated

import psycopg2  # type: ignore
from fastapi import Depends, FastAPI, File, HTTPException
from fastapi.responses import HTMLResponse

from .connect import get_conn
from .models import Analysis

app = FastAPI()


@app.get("/")
async def main():
    content = """
<body>
<form action="/upload" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.post("/upload")
async def upload_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/analyses/")
def add_analysis(analysis: Analysis, conn = Depends(get_conn)) -> Analysis:
    if analysis.id is None:
        analysis.id = str(uuid.uuid4())
    
    for data_file in analysis.data_files:
        data_file.is_uploaded = False

    data_files_json = json.dumps([data_file.model_dump() for data_file in analysis.data_files])
    
    query = "INSERT INTO analyses (id, owners, data_files, statistical_method) VALUES (%s, %s, %s, %s);"
    
    with conn.cursor() as cur:
        cur.execute(query, (analysis.id, analysis.owners, data_files_json, analysis.statistical_method.value))
        conn.commit()
        
    return analysis


@app.get("/analyses")
def get_analysis_by_owner(owner: str, conn = Depends(get_conn)) -> list[Analysis]:
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM analyses WHERE owners @> ARRAY['{owner}'];")
        result = cur.fetchall()
    
    return [
        Analysis(
            id=row[0],
            owners=row[1],
            data_files=row[2],
            statistical_method=row[3],
            method_arguments=row[4],
        )
        for row in result
    ]


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
        data_files=result[2],
        statistical_method=result[3],
        method_arguments=result[4],
    )
