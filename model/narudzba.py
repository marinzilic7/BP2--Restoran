from __init__ import Base

from sqlalchemy import *
from sqlalchemy.orm import relationship

class Narudzba (Base):
    __tablename__ = "narudzba"
    ID_narudzba = Column(Integer, primary_key = True)
    korisnik_id = Column(Integer, ForeignKey('korisnici.ID_korisnika'))
    naziv = Column(String(50))
    cijena =Column(Integer)
   