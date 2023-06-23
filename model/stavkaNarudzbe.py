from __init__ import Base

from sqlalchemy import *
from sqlalchemy.orm import relationship

class StavkaNarudzbe (Base):
    __tablename__ = "stavka_narudzbe"
    ID_narudzba = Column(Integer, primary_key = True)
    korisnik_id = Column(Integer, ForeignKey('korisnici.ID_korisnika'))
    jelo_id = Column(Integer,ForeignKey('hrana.ID_food'))
    pice_id = Column(Integer,ForeignKey('drinks.ID_drink'))
    kolicina =Column(Integer)
   