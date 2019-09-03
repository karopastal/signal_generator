import json
import flask
from flask import request, jsonify, send_from_directory, send_file
from flask_cors import CORS
from api import *

app = flask.Flask(__name__, static_folder='static/vue-material-dashboard-master/dist', static_url_path='')
app.config["CACHE_TYPE"] = "null"
app.config["DEBUG"] = True
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/v1/resources/signals', methods=['GET'])
def signals():
    return jsonify(all_signals())


@app.route('/api/v1/resources/backgrounds', methods=['GET'])
def backgrounds():
    return jsonify(all_backgrounds())


@app.route('/api/v1/resources/wavelets', methods=['GET'])
def wavelets():
    return jsonify(all_wavelets())


@app.route('/api/v1/resources/update_signal', methods=['POST'])
def update_signal():
    update_signals(data=request.json)
    return jsonify({'status': 'ok'})


@app.route('/api/v1/resources/new_signal', methods=['POST'])
def new_signal():
    new_signals(data=request.json)
    return jsonify({'status': 'ok'})


@app.route('/api/v1/resources/delete_signal', methods=['POST'])
def delete_signal():
    delete_signals(id=request.json['id'])
    return jsonify({'status': 'ok'})


@app.route('/api/v1/resources/update_background', methods=['POST'])
def update_background():
    update_backgrounds(data=request.json)
    return jsonify({'status': 'ok'})


@app.route('/api/v1/resources/new_background', methods=['POST'])
def new_background():
    new_backgrounds(data=request.json)
    return jsonify({'status': 'ok'})


@app.route('/api/v1/resources/delete_background', methods=['POST'])
def delete_background():
    delete_backgrounds(id=request.json['id'])
    return jsonify({'status': 'ok'})


@app.route('/api/v1/resources/update_wavelet', methods=['POST'])
def update_wavelet():
    update_wavelets(data=request.json)
    return jsonify({'status': 'ok'})


@app.route('/api/v1/resources/new_wavelet', methods=['POST'])
def new_wavelet():
    new_wavelets(data=request.json)
    return jsonify({'status': 'ok'})


@app.route('/api/v1/resources/delete_wavelet', methods=['POST'])
def delete_wavelet():
    delete_wavelets(id=request.json['id'])
    return jsonify({'status': 'ok'})


@app.route('/gallery/<path>')
def gallery(path):
    return send_file(app.static_folder + '/gallery/' + path)


app.run()
