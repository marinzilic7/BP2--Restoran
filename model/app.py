from __init__ import session
from jelo import Jelo


import os 

from flask import Flask,render_template



app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))



@app.route("/")
def index ():
    jela = session.query(Jelo).all()
    return render_template('home.html', jelo=jela)


if __name__ == '__main__':
    app.run()