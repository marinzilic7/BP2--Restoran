from . import Base

from sqlalchemy import *
from sqlalchemy.orm import relationship

class Drinks (Base):
    __tablename__ = "drinks"
    ID_drink = Column(Integer, primary_key = True)
    naziv = Column(String(50))
    cijena =Column(Integer(50))
   