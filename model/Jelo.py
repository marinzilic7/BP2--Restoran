from __init__ import Base
from sqlalchemy import *

class Jelo (Base):
    __tablename__ = "hrana"
    ID_food = Column(Integer, primary_key = True)
    ID_kategorija = Column(Integer,ForeignKey('kategorija.ID_kategorija'))
    naziv = Column(String(50))
    opis = Column(String(50))
    cijena =Column(Integer)
   