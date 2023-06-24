from __init__ import Base

from sqlalchemy import *


class Pice (Base):
    __tablename__ = "drinks"
    ID_drink = Column(Integer, primary_key = True)
    naziv = Column(String(50))
    cijena =Column(Integer)
    kategorija_id= Column(Integer, ForeignKey('kategorija.ID_kategorija'))