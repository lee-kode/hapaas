from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/frontend')
def handle_frontend():
    return 'Hello, frontend!'


@app.route('/api/v1/backend')
def handle_backend():
    return 'Hello, backend!'


@app.route('/api/v1/listen')
def handle_listen():
    return 'Hello, listen!'

