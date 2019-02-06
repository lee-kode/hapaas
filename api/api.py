from flask import Flask, json, jsonify, request, make_response
from lib.config import get_config
from lib.db import HapaasRedis

app = Flask(__name__)
config = get_config()
api_base_url = "http://{}:{}/api/v1".format(config.get('api','host'), config.get('api','port'))


@app.route('/config')
def handle_config():
    return jsonify(config)


@app.route('/api/v1/frontend', methods=['GET'])
def handle_frontend_list():
    results = []

    for key in sorted(HapaasRedis().scan_iter("frontend:*")):
        results.append("{}/frontend/{}".format(api_base_url, key.replace('frontend:', '')))

    return jsonify(results)


@app.route('/api/v1/frontend/<frontend>', methods=['GET'])
def handle_frontend_get(frontend):
    fe = HapaasRedis().get('frontend:{}'.format(frontend))

    if fe:
        return jsonify(json.loads(fe))
    else:
        return make_response(jsonify({'message': 'Frontend not found.'}), 404)


@app.route('/api/v1/frontend', methods=['POST'])
def handle_frontend_create():
    if request.is_json:
        # 1.) Persist to database
        # TODO: input validation
        frontend_json = request.get_json()
        frontend_json['state'] = 'new'
        name = frontend_json['name']
        resp = HapaasRedis().set('frontend:{}'.format(name), json.dumps(frontend_json))

        if resp:
            # 2.) Send packet to broker
            pass
        else:
            return make_response(jsonify({'message': 'Could not persist object to database.'}), 512)

        # 3.) Respond
        return jsonify(message="Request has been sucessfully received.")

    return jsonify(message="Hello, frontend!")


@app.route('/api/v1/frontend/<frontend>', methods=['PUT', 'DELETE'])
def handle_frontend_mutate(frontend):
    if request.method == 'PUT':
        # Update the row
        pass

    if request.method == 'DELETE':
        # Delete the row
        pass

    return jsonify(message="Hello, frontend!")


@app.route('/api/v1/backend')
def handle_backend():
    return jsonify(message="Hello, backend!")


@app.route('/api/v1/listen')
def handle_listen():
    return jsonify(message="Hello, listen!")


if __name__ == '__main__':
    host = config.get('api', 'host')
    port = config.get('api', 'port')

    app.run(host=host, port=port)
