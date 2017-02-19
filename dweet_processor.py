from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import TextField

import urllib2
import json

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://nleong:420dankmemes420@pollappdb-cluster.cluster-cijys1vqvqce.us-west-2.rds.amazonaws.com'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/', methods=['POST', 'GET'])
def get_data(data=None):

    request_link = 'https://thingspace.io/get/dweets/for/test111'

    req_dweet = urllib2.urlopen(request_link)
    dweet = json.load(req_dweet)


    amt_dweets = len(dweet['with'])

    d = []

    for i in range(0, amt_dweets-1):
        d.append(dweet['with'][i]['created'])

    return render_template('answer_page.html', data=d)



@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()