import json
from sqlalchemy.orm import Session
from .models import Usina, Inversor

def populate_db_from_json(db: Session, file_path: str):
    with open(file_path) as f:
        data = json.load(f)

    for usina_data in data['usinas']:
        usina = Usina(nome=usina_data['nome'])
        db.add(usina)
        db.commit()
        db.refresh(usina)
        
        for inversor_data in usina_data['inversores']:
            inversor = Inversor(
                usina_id=usina.id,
                nome=inversor_data['nome'],
                potencia_ativa=inversor_data['potencia_ativa'],
                temperatura=inversor_data['temperatura'],
                data=inversor_data['data']
            )
            db.add(inversor)
            db.commit()
