from db import user_data
from model.user import User

from flask import request, make_response, Blueprint

bp = Blueprint("user", __name__, url_prefix="/")


@bp.route("/user/<user_id>", methods=["GET"])
def user_get(user_id):
    user = user_data.get(user_id)
    if user:
        resp = make_response(user.to_dict())
        status = 200
    else:
        resp = make_response({"error": "user not found man"})
        status = 404

    return resp, status


@bp.route("/user", methods=["POST"])
def user_create():
    body = request.json
    u = User(name=body.get('name'), age=body.get('age'), skills=body.get('skills'))
    user_data[u.uid] = u
    resp = make_response(u.to_dict())
    status = 201
    return resp, status


@bp.route("/user/<user_id>", methods=["PUT"])
def user_update(user_id):
    user = user_data.get(user_id)
    if not user:
        resp = make_response({"error": "user not found man"})
        status = 404
        return resp, status

    body = request.json
    if "name" in body:
        user.name = body.get('name')
    if "age" in body:
        user.age = body.get("age")
    if "skills" in body:
        user.skills = body.get('skills')

    user_data[user_id] = user
    resp = make_response(user.to_dict())
    status = 201
    return resp, status
