from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import json

from . import models, crud, schemas
from .database import SessionLocal, engine

# Iniciar o banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD para Usinas
@app.post("/usinas/", response_model=schemas.Usina)
def create_usina(usina: schemas.UsinaCreate, db: Session = Depends(get_db)):
    return crud.create_usina(db=db, usina=usina)

@app.get("/usinas/{usina_id}", response_model=schemas.Usina)
def get_usina(usina_id: int, db: Session = Depends(get_db)):
    db_usina = crud.get_usina(db, usina_id=usina_id)
    if db_usina is None:
        raise HTTPException(status_code=404, detail="Usina not found")
    return db_usina

# CRUD para Inversores
@app.post("/inversores/", response_model=schemas.Inversor)
def create_inversor(inversor: schemas.InversorCreate, db: Session = Depends(get_db)):
    return crud.create_inversor(db=db, inversor=inversor)

@app.get("/inversores/{inversor_id}", response_model=schemas.Inversor)
def get_inversor(inversor_id: int, db: Session = Depends(get_db)):
    db_inversor = crud.get_inversor(db, inversor_id=inversor_id)
    if db_inversor is None:
        raise HTTPException(status_code=404, detail="Inversor not found")
    return db_inversor

# Endpoint para Potência Máxima por Dia
@app.get("/potencia_maxima_por_dia/")
def potencia_maxima_por_dia(inversor_id: int, data_inicio: str, data_fim: str, db: Session = Depends(get_db)):
    return crud.get_potencia_maxima_por_dia(db, inversor_id, data_inicio, data_fim)

# Endpoint para Geração por Usina
@app.get("/geracao_usina/")
def geracao_usina(usina_id: int, data_inicio: str, data_fim: str, db: Session = Depends(get_db)):
    return crud.get_geracao_usina(db, usina_id, data_inicio, data_fim)

# Endpoint para Geração por Inversor
@app.get("/geracao_inversor/")
def geracao_inversor(inversor_id: int, data_inicio: str, data_fim: str, db: Session = Depends(get_db)):
    return crud.get_geracao_inversor(db, inversor_id, data_inicio, data_fim)
