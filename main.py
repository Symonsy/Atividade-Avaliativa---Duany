from fastapi import FastAPI, HTTPException, Query
from uuid import UUID
from datetime import datetime
from typing import Optional
from schemas import ProjectCreate, ProjectUpdate, ProjectResponse
from models import db, generate_id
from fastapi import Path
from uuid import UUID

app = FastAPI()

from fastapi.responses import Response

@app.delete("/projects/{project_id}", status_code=204)
def delete_project(project_id: UUID):
    pid = str(project_id)
    if pid not in db:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    del db[pid]
    return Response(status_code=204)

@app.get("/projects/{project_id}", response_model=ProjectResponse)
def get_project(project_id: UUID = Path(...)):
    project = db.get(str(project_id))
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return project

@app.put("/projects/{project_id}", response_model=ProjectResponse)
def update_project(project_id: UUID, project_update: ProjectUpdate):
    pid = str(project_id)
    existing = db.get(pid)
    if not existing:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    updated_data = project_update.dict()
    updated_project = {
        **existing,
        **updated_data  
    }

    db[pid] = updated_project
    return updated_project


@app.post("/projects", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreate):
    id = generate_id()
    now = datetime.now()
    data = project.dict()
    data.update({"ID": id, "Criado em": now})
    db[str(id)] = data  
    return data

@app.get("/projects", response_model=list[ProjectResponse])
def list_projects(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=100),
    status: Optional[str] = Query(None),
    priority: Optional[int] = Query(None)
):
    results = list(db.values())
    if status:
        results = [p for p in results if p["status"] == status]
    if priority:
        results = [p for p in results if p["P        git commit -m "Commit inicial do projeto"rioridade"] == priority]
    return results[skip : skip + limit]
