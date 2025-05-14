from pydantic import BaseModel
from typing import List, Optional

class InversorBase(BaseModel):
    nome: str
    potencia_ativa: float
    temperatura: float
    data: str

class InversorCreate(InversorBase):
    usina_id: int

class Inversor(InversorBase):
    id: int
    usina_id: int

    class Config:
        orm_mode = True

class UsinaBase(BaseModel):
    nome: str

class UsinaCreate(UsinaBase):
    pass

class Usina(UsinaBase):
    id: int
    inversores: List[Inversor] = []

    class Config:
        orm_mode = True
