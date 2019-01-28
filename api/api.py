from flask import Flask, json, jsonify

app = Flask(__name__)


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
    # TODO: This must get pulled from an config object
    host = '127.0.0.1'
    port = 8080

    app.run(host=host, port=port)
