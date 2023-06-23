from sqlalchemy.orm import relationship

from sqlalchemy.orm import relationship
from korisnik import Korisnik
from narudzba import Narudzba
from stavka import Stavka
from pice import Pice
from jelo import Jelo

from __init__ import Base
from __init__  import engine


Korisnik.naruzba = relationship('Narudzba', back_populates='korisnik')
Narudzba.stavka = relationship('Stavka', back_populates='narudzba')
Jelo.stavka = relationship('Stavka', back_populates='hrana')
Pice.stavka = relationship('Stavka', back_populates='drinks')

Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)