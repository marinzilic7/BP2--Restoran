
from sqlalchemy.orm import relationship
from korisnik import Korisnik
from narudzba import Narudzba
from pice import Pice
from jelo import Jelo
from kategorija import Kategorija
from stavkaNarudzbe import StavkaNarudzbe
from __init__ import Base
from __init__  import engine


Korisnik.naruzba = relationship('Narudzba', back_populates='korisnik')
Narudzba.stavka = relationship('StavkaNarudzbe', back_populates='narudzba')
Jelo.stavka = relationship('StavkaNarudzbe', back_populates='hrana')
Pice.stavka = relationship('StavkaNarudzbe', back_populates='drinks')
Jelo.kategorija = relationship('Kategorija', back_populates='hrana')
Pice.kategorija = relationship('Kategorija', back_populates='drinks')

Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)