from flask import Blueprint, jsonify, g
from rethinkdb import RethinkDB

r = RethinkDB()
api = Blueprint('services', __name__)

# Routes:
#
# GET     /services/:id/widgets
# GET     /services/:id/widgets/:id

def get_current_id(r):
    cursor = r.table('services').run(g.conn)
    services = list(cursor)

    if len(services) == 0:
        return 0

    index = r.table('services').max('id')['id'].run(g.conn)

    return index

def get_next_id(r):
    return get_current_id(r) + 1

@api.route('/', methods = ['GET'])
def services():
    cursor = r.table('services').order_by('id').run(g.conn)
    services = list(cursor)

    return jsonify(
                status = 200,
                message = 'OK',
                success = True,
                data = services
            ), 200

@api.route('/<id>', methods = ['GET'])
def service(id):
    if id.isdigit():
        id = int(id)
    else:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('services').run(g.conn)
    services = list(cursor)

    if id == 0 or len(services) < id:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('services').get(id).run(g.conn)

    return jsonify(
                status = 200,
                message = 'OK',
                success = True,
                data = cursor
            ), 200
