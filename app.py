from flask import Flask
from flask import request, make_response
from db import state_data, user_data
from handlers import user_handler

app = Flask(__name__)
app.register_blueprint(user_handler.bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/health', methods=['GET'])
def health():
    args = request.args
    resp_dict = dict()
    status = 200
    if args.get('name') == 'foo':
        resp_dict['status'] = state_data
    elif args.get('name') == 'bar':
        resp_dict['status'] = 'up'
    else:
        status = 404
    resp = make_response(resp_dict)
    return resp, status


@app.route('/appstate', methods=['POST'])
def set_state():
    body = request.json
    state_data.update(body)
    resp = make_response({"status": "Success"})
    resp.status_code = 201
    return resp


def get_app() -> Flask:
    return app


if __name__ == '__main__':
    app.run()
else:
    get_app()
