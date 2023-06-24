
from sqlalchemy.orm import relationship
from korisnik import Korisnik
from narudzba import Narudzba
from pice import Pice
from jelo import Jelo
from kategorija import Kategorija
from __init__ import Base
from __init__  import engine


Korisnik.narudzba = relationship('Narudzba', back_populates='korisnik')
Narudzba.stavka = relationship('StavkaNarudzbe', back_populates='narudzba')
Jelo.kategorija = relationship('Kategorija', back_populates='hrana')
Pice.kategorija = relationship('Kategorija', back_populates='drinks')
Kategorija.jelo = relationship('Jelo', back_populates='kategorija')

Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)