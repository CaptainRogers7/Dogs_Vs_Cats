# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 02:16:39 2020

@author: pushk
"""

from flask import request
from flask import jsonify
from flask import Flask
import json as json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS-HEADERS']='Content-Type'

@app.route('/hello',methods=['POST'])
@cross_origin()
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
            'greeting': 'Hello, '+ name +'!'
    }
    return jsonify(response)