from flask import Flask, json, jsonify

from lib.config import get_config

app = Flask(__name__)
config = get_config()


@app.route('/config')
def handle_config():
    return jsonify(config)


@app.route('/api/v1/frontend')
def handle_frontend():
    return jsonify(message="Hello, frontend!")


@app.route('/api/v1/backend')
def handle_backend():
    return jsonify(message="Hello, backend!")


@app.route('/api/v1/listen')
def handle_listen():
    return jsonify(message="Hello, listen!")


if __name__ == '__main__':
    host = config['api']['host']
    port = config['api']['port']

    app.run(host=host, port=port)
