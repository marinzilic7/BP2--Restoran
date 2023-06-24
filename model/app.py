from __init__ import session
from jelo import Jelo


import os 

from flask import Flask,render_template, request,redirect, url_for



app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))



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


if __name__ == '__main__':
    app.run()