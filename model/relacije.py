from sqlalchemy.orm import relationship

from sqlalchemy.orm import relationship
from korisnik import Korisnik
from narudzba import Narudzba
from stavka import Stavka
from Pice import Drinks
from Jelo import Food

from __init__ import Base
from __init__  import engine


Korisnik.naruzba = relationship('Narudzba', back_populates='korisnik')
Narudzba.stavka = relationship('Stavka', back_populates='narudzba')
Food.stavka = relationship('Stavka', back_populates='hrana')
Drinks.stavka = relationship('Stavka', back_populates='drinks')

Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)