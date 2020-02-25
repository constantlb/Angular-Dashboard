from flask import Blueprint, jsonify, g
from rethinkdb import RethinkDB

r = RethinkDB()
api = Blueprint('widgets', __name__)

def get_current_id(r):
    cursor = r.table('widgets').run(g.conn)
    widgets = list(cursor)

    if len(widgets) == 0:
        return 0

    index = r.table('widgets').max('id')['id'].run(g.conn)

    return index

def get_next_id(r):
    return get_current_id(r) + 1

@api.route('/', methods = ['GET'])
def widgets():
    cursor = r.table('widgets').order_by('id').run(g.conn)
    widgets = list(cursor)

    return jsonify(
                status = 200,
                message = 'OK',
                success = True,
                data = widgets
            ), 200

@api.route('/<id>', methods = ['GET'])
def widget(id):
    if id.isdigit():
        id = int(id)
    else:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('widgets').run(g.conn)
    widgets = list(cursor)

    if id == 0 or len(widgets) < id:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('widgets').get(id).run(g.conn)

    return jsonify(
                status = 200,
                message = 'OK',
                success = True,
                data = cursor
            ), 200
