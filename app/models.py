from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Usina(Base):
    __tablename__ = "usinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

class Inversor(Base):
    __tablename__ = "inversores"

    id = Column(Integer, primary_key=True, index=True)
    usina_id = Column(Integer, ForeignKey('usinas.id'))
    nome = Column(String, index=True)
    potencia_ativa = Column(Float)
    temperatura = Column(Float)
    data = Column(String)

    usina = relationship("Usina", back_populates="inversores")

Usina.inversores = relationship("Inversor", back_populates="usina")
