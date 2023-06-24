from __init__ import session
from jelo import Jelo
from kategorija import Kategorija


import os 

from flask import Flask,render_template, request,redirect, url_for,flash



app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))
app.secret_key = 'ovo-je-moj-tajni-kljuc'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def index ():
    jela = session.query(Jelo).all()
    return render_template('home.html', jela=jela)

@app.route('/dodaj-jelo', methods=['POST'])
def dodaj_jelo():
    naziv = request.form.get('naziv')
    opis = request.form.get('opis')
    cijena = int(request.form.get('cijena'))

    novo_jelo = Jelo(naziv=naziv, opis=opis, cijena=cijena)
    session.add(novo_jelo)
    session.commit()

    
    return redirect(url_for('index'))


@app.route("/kategorija")
def kategorija():
    kategorije = session.query(Kategorija).all()
    return render_template('kategorija.html', kategorije=kategorije)

 

@app.route('/dodaj-kategoriju', methods=['POST'])
def dodaj_kategoriju():
    naziv = request.form.get('naziv')

    nova_kategorija = Kategorija(naziv=naziv)
    session.add(nova_kategorija)
    session.commit()

    flash('Kategorija je uspješno dodana.', 'success')
    return redirect(url_for('kategorija'))


@app.route('/izbrisi_kategoriju/<int:ID_kategorija>', methods=['POST'])
def izbrisi_kategoriju(ID_kategorija):
    kategorija = session.query(Kategorija).get(ID_kategorija)
    print(kategorija)
    if kategorija:
        # Izbriši kategoriju iz baze podataka
        session.delete(kategorija)
        session.commit()
        flash('Kategorija je uspješno obrisana.', 'warning')
    else:
        flash('Kategorija nije pronađena.', 'error')

    return redirect(url_for('kategorija'))


if __name__ == '__main__':
    app.run()