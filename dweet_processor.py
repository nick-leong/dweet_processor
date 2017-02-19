from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import TextField

import urllib2
import json

app = Flask(__name__)
app.debug = True

dweet = 'https://thingspace.io/dweet/for/dweet_game_input?'

ident = 0;

@app.route('/', methods=['POST', 'GET'])
def send_dweet(dweet = dweet):

    global ident

    if ident == 0:
        ident = 1
    elif ident == 1:
        ident = 0

    if request.method == 'POST':
        if request.form['submit'] == 'up':
            dweet += 'direction=u'
            dweet += str(ident)
        
        elif request.form['submit'] == 'down':
            dweet += 'direction=d'
            dweet += str(ident)
        
        elif request.form['submit'] == 'right':
            dweet += 'direction=r'
            dweet += str(ident)
        
        elif request.form['submit'] == 'left':
            dweet += 'direction=l'
            dweet += str(ident)

    urllib2.urlopen(dweet)

    return render_template('test.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()