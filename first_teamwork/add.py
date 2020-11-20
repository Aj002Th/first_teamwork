#  add.py
#  coding=gbk

from flask import Blueprint, request
from database import save_add
from utils import HttpError

add_bp = Blueprint('add', __name__, url_prefix='/add')


@add_bp.route('', methods=['POST'])
def add_users():
    data = request.get_json(force=True)  # ����ǰ�˵���������
    username = data.get('name')
    student_nums = data.get('num')

    if username is None and student_nums is None:
        raise HttpError(400, 'ȱ�ٲ��� name\n ȱ�ٲ��� num')
    if username is None:
        raise HttpError(400, 'ȱ�ٲ��� name')
    if student_nums is None:
        raise HttpError(400, 'ȱ�ٲ��� num')

    save_add(username, student_nums)

    return '��ӳɹ�'
