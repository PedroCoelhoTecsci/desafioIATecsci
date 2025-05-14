from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import func

# Criar Usina
def create_usina(db: Session, usina: schemas.UsinaCreate):
    db_usina = models.Usina(nome=usina.nome)
    db.add(db_usina)
    db.commit()
    db.refresh(db_usina)
    return db_usina

# Criar Inversor
def create_inversor(db: Session, inversor: schemas.InversorCreate):
    db_inversor = models.Inversor(
        usina_id=inversor.usina_id,
        nome=inversor.nome,
        potencia_ativa=inversor.potencia_ativa,
        temperatura=inversor.temperatura,
        data=inversor.data,
    )
    db.add(db_inversor)
    db.commit()
    db.refresh(db_inversor)
    return db_inversor

# Potência máxima por dia
def get_potencia_maxima_por_dia(db: Session, inversor_id: int, data_inicio: str, data_fim: str):
    return db.query(func.max(models.Inversor.potencia_ativa)).filter(
        models.Inversor.id == inversor_id,
        models.Inversor.data >= data_inicio,
        models.Inversor.data <= data_fim
    ).first()

# Geração por Usina
def get_geracao_usina(db: Session, usina_id: int, data_inicio: str, data_fim: str):
    return db.query(func.sum(models.Inversor.potencia_ativa)).filter(
        models.Inversor.usina_id == usina_id,
        models.Inversor.data >= data_inicio,
        models.Inversor.data <= data_fim
    ).first()

# Geração por Inversor
def get_geracao_inversor(db: Session, inversor_id: int, data_inicio: str, data_fim: str):
    return db.query(func.sum(models.Inversor.potencia_ativa)).filter(
        models.Inversor.id == inversor_id,
        models.Inversor.data >= data_inicio,
        models.Inversor.data <= data_fim
    ).first()
