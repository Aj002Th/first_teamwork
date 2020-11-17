#  users.py
#  coding=gbk

from flask import Blueprint, jsonify
from database import find_all_users

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('')
def show_users_list():
    list_before_fixed = find_all_users()
    list_fixed = [x[0] for x in list_before_fixed]
    response = jsonify(list_fixed)
    return response

