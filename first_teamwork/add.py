#  add.py
#  coding=gbk

from flask import Blueprint, request
from database import save_add
from utils import HttpError

add_bp = Blueprint('add', __name__, url_prefix='/add')


@add_bp.route('', methods=['POST'])
def add_users():
    data = request.get_json(force=True)  # 捕获前端的请求内容
    username = data.get('name')
    student_nums = data.get('num')

    if username is None and student_nums is None:
        raise HttpError(400, '缺少参数 name\n 缺少参数 num')
    if username is None:
        raise HttpError(400, '缺少参数 name')
    if student_nums is None:
        raise HttpError(400, '缺少参数 num')

    save_add(username, student_nums)

    return '添加成功'
