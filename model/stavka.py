from __init__ import Base

from sqlalchemy import *
from sqlalchemy.orm import relationship

class Stavka (Base):
    __tablename__ = "Stavka"
    id_stavke = Column(Integer, primary_key = True)
    narudzba_id = Column(Integer, ForeignKey('narudzba.ID_narudzba'))
    jelo_id = Column(Integer,ForeignKey('hrana.ID_food'))
    pice_id = Column(Integer,ForeignKey('drinks.ID_drink'))
    kolicina = Column(Integer())