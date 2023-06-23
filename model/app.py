
from flask import Flask, request, render_template
from flask import jsonify
import json
from kafka import KafkaProducer, KafkaConsumer
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import threading
from __init__ import session
from jelo import Jelo
import os
from flask import Flask

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))


@app.route("/")
def index():
    jela = session.query(Jelo).all()
    return render_template('home.html', jela=jela)

if __name__ == '__main__':
    app.run()