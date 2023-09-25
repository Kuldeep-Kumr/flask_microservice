from functools import wraps

from flask import Blueprint, jsonify, request

from user_microservices.database.db import get_db
from user_microservices.database.models import USER_DATA

bp = Blueprint('api', __name__, url_prefix='/api')


def __fetch_all_user():
    db = get_db()
    __data = []
    index_count = 1
    __object_from_table_data = db.session.query(USER_DATA).all()
    for __object_data in __object_from_table_data:
        # converting the object into dictionary format
        __dic_of_data = __object_data.__dict__
        __object_of_user_data = {}
        __object_of_user_data['INDEX'] = index_count
        __object_of_user_data['ID'] = str(__dic_of_data['ID'])
        __object_of_user_data['USERNAME'] = __dic_of_data['USERNAME']
        index_count += 1
        __data.append(__object_of_user_data)
    return __data


def __add_new_user(__data):
    db = get_db()
    __object_of_data = USER_DATA(
        username=__data['username'],
        password=__data['password']
    )
    db.session.add(__object_of_data)
    db.session.commit()


@bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        __data = request.get_json()
        __add_new_user(__data)
        return jsonify({'message': "User added successfully"})
    return jsonify({'message': "Invaild Call"})


@bp.route('/all_user', methods=['GET', 'POST'])
def all_user():
    if request.method == 'GET':
        return jsonify(__fetch_all_user())

    return jsonify({'message': 'Invalid Call'})
