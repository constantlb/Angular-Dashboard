from flask import Blueprint, jsonify, g, request
from rethinkdb import RethinkDB
from data import get_data

r = RethinkDB()
api = Blueprint('users', __name__)

# Routes:
#
# POST    /users/:id
# POST    /users/:id/widgets/:id
#
# DELETE  /users/:id/connections/:name
# GET     /users/:id/connections/:name
# POST    /users/:id/connections/:name

def get_current_user_id(r):
    cursor = r.table('users').run(g.conn)
    users = list(cursor)

    if len(users) == 0:
        return 0

    index = r.table('users').max('id')['id'].run(g.conn)

    return index

def get_next_user_id(r):
    return get_current_user_id(r) + 1

def get_current_widget_id(r, user_id):
    cursor = r.table('users').get(user_id)['widgets'].run(g.conn)
    widgets = list(cursor)

    if len(widgets) == 0:
        return 0

    index = r.table('users').get(user_id)['widgets'].max('id')['id'].run(g.conn)

    return index

def get_next_widget_id(r, user_id):
    return get_current_widget_id(r, user_id) + 1

def is_valid(x):
    return x is not None

def is_str_valid(str):
    return is_valid(str) and not str.isspace()

@api.route('/', methods = ['GET', 'POST'])
def users():
    if request.method == 'GET':
        cursor = r.table('users').without('connections', 'password', 'widgets').order_by('id').run(g.conn)
        users = list(cursor)

        return jsonify(
                    status = 200,
                    message = 'OK',
                    success = True,
                    data = users
                ), 200
    else:
        json = request.get_json()

        if json is not None:
            if 'username' not in json or 'email' not in json or 'password' not in json:
                return jsonify(
                        status = 400,
                        message = 'Bad Request',
                        success = False,
                        data = None
                    ), 400

            username = json['username']
            email = json['email']
            password = json['password']
        else:
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

        if is_str_valid(username) and is_str_valid(email) and is_str_valid(password):

            cursor = r.table('users').filter({
                            'email': email
                        }).run(g.conn)

            users = list(cursor)

            if len(users) != 0:
                return jsonify(
                            status = 400,
                            message = 'Bad Request',
                            success = False,
                            data = None
                        ), 400

            cursor = r.table('users').insert({
                            'id': get_next_user_id(r),
                            'username': username,
                            'email': email,
                            'password': password,
                            'creation_date': r.now().to_epoch_time(),
                            'widgets': [],
                            'connections': []
                        }, return_changes = True).run(g.conn)

            return jsonify(
                        status = 201,
                        message = 'Created',
                        success = True,
                        data = {
                            'creation_date': cursor['changes'][0]['new_val']['creation_date'],
                            'email': cursor['changes'][0]['new_val']['email'],
                            'id': cursor['changes'][0]['new_val']['id'],
                            'username': cursor['changes'][0]['new_val']['username']
                        }
                    ), 201

    return jsonify(
                status = 400,
                message = 'Bad Request',
                success = False,
                data = None
            ), 400

@api.route('/login', methods = ['POST'])
def login():
    json = request.get_json(force = True)

    if json is not None:
        if 'email' not in json or 'password' not in json:
            return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

        email = json['email']
        password = json['password']
    else:
        email = request.form.get('email')
        password = request.form.get('password')

    if is_str_valid(email) and is_str_valid(password):
        cursor = r.table('users').filter({
                        'email': email,
                        'password': password
                    }, default = False).without('connections', 'password', 'widgets').run(g.conn)

        users = list(cursor)

        if len(users) == 1:
            return jsonify(
                    status = 200,
                    message = 'OK',
                    success = True,
                    data = users[0]
                ), 200

    return jsonify(
                status = 400,
                message = 'Bad Request',
                success = False,
                data = None
            ), 400

@api.route('/<user_id>', methods = ['GET', 'DELETE'])
def user(user_id):
    if user_id.isdigit():
        user_id = int(user_id)
    else:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('users').get(user_id).run(g.conn)

    if cursor is None:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    if request.method == 'GET':
        cursor = r.table('users').get(user_id).without('connections', 'password', 'widgets').run(g.conn)

        return jsonify(
                    status = 200,
                    message = 'OK',
                    success = True,
                    data = cursor
                ), 200
    else:
        cursor = r.table('users').get(user_id).delete().run(g.conn)

        return jsonify(
                    status = 200,
                    message = 'OK',
                    success = True,
                    data = None
                ), 200

    return jsonify(
                status = 400,
                message = 'Bad Request',
                success = False,
                data = None
            ), 400

@api.route('/<user_id>/connections', methods = ['GET', 'POST'])
def connections(user_id):
    if user_id.isdigit():
        user_id = int(user_id)
    else:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('users').get(user_id).run(g.conn)

    if cursor is None:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    if request.method == 'GET':
        cursor = r.table('users').get(user_id).run(g.conn)

        return jsonify(
                    status = 200,
                    message = 'OK',
                    success = True,
                    data = cursor['connections']
                ), 200
    else:
        json = request.get_json()

        if json is not None:
            if 'name' not in json or 'token' not in json:
                    return jsonify(
                        status = 400,
                        message = 'Bad Request',
                        success = False,
                        data = None
                    ), 400

            name = json['name']
            token = json['token']
        else:
            name = request.form.get('name')
            token = request.form.get('token')

        if is_str_valid(name) and is_str_valid(token):
            cursor = r.table('users').get(user_id).update({
                    'connections': r.row['connections'].append({
                        'name': name,
                        'token': token
                    })
                }, return_changes = True).run(g.conn)

    return jsonify(
                status = 201,
                message = 'Created',
                success = True,
                data = {
                    'name': cursor['changes'][0]['new_val']['connections'][-1]['name'],
                    'token': cursor['changes'][0]['new_val']['connections'][-1]['token']
                }
            ), 201

    return jsonify(
            status = 400,
            message = 'Bad Request',
            success = False,
            data = None
        ), 400

@api.route('/<user_id>/widgets', methods = ['GET', 'POST'])
def widgets(user_id):
    if user_id.isdigit():
        user_id = int(user_id)
    else:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('users').get(user_id).run(g.conn)

    if cursor is None:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    if request.method == 'GET':
        cursor = r.table('users').get(user_id).run(g.conn)

        return jsonify(
                    status = 200,
                    message = 'OK',
                    success = True,
                    data = cursor['widgets']
                ), 200
    else:
        json = request.get_json()

        if json is not None:
            if 'type' not in json or 'refresh_time' not in json or 'params' not in json or 'position' not in json:
                return jsonify(
                        status = 400,
                        message = 'Bad Request',
                        success = False,
                        data = None
                    ), 400

            type = json['type']
            refresh_time = json['refresh_time']
            params = json['params']
            position = json['position']
        else:
            type = request.form.get('type')
            refresh_time = request.form.get('refresh_time')
            params = request.form.get('params')
            position = request.form.get('position')

        if is_str_valid(type) and is_valid(refresh_time) and is_valid(params) and is_valid(position):
            cursor = r.table('users').get(user_id).update({
                            'widgets': r.row['widgets'].append({
                                'id': get_next_widget_id(r, user_id),
                                'type': type,
                                'params': params,
                                'position': position
                            })
                        }, return_changes = True).run(g.conn)

            return jsonify(
                        status = 201,
                        message = 'Created',
                        success = True,
                        data = {
                            'id': cursor['changes'][0]['new_val']['widgets'][-1]['id'],
                            'type': cursor['changes'][0]['new_val']['widgets'][-1]['type'],
                            'params': cursor['changes'][0]['new_val']['widgets'][-1]['params'],
                            'position': cursor['changes'][0]['new_val']['widgets'][-1]['position']
                        }
                    ), 201

    return jsonify(
            status = 400,
            message = 'Bad Request',
            success = False,
            data = None
        ), 400

@api.route('/<user_id>/widgets/<widget_id>', methods = ['GET', 'DELETE'])
def widget(user_id, widget_id):
    if user_id.isdigit():
        user_id = int(user_id)
    else:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    if widget_id.isdigit():
        widget_id = int(widget_id)
    else:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('users').get(user_id).run(g.conn)

    if cursor is None:
        return jsonify(
                    status = 400,
                    message = 'Bad Request: ',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('users').get(user_id)['widgets'].contains(lambda widget:
        widget['id'].eq(widget_id)
    ).run(g.conn)

    if not cursor:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    if request.method == 'GET':
        cursor = r.table('users').get(user_id)['widgets'].filter({
                        'id': widget_id
                    }).run(g.conn)
        widgets = list(cursor)

        if len(widgets) == 1:
            return jsonify(
                        status = 200,
                        message = 'OK',
                        success = True,
                        data = cursor[0]
                    ), 200

        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400
    else:
        cursor = r.table('users').get(user_id).update(lambda doc:
                        doc.merge({
                            'widgets': doc['widgets'].filter(lambda widget:
                                widget['id'].ne(widget_id)
                            )
                        })
                    ).run(g.conn)

        return jsonify(
                    status = 200,
                    message = 'OK',
                    success = True,
                    data = None
                ), 200

    return jsonify(
            status = 400,
            message = 'Bad Request',
            success = False,
            data = None
        ), 400

@api.route('/<user_id>/widgets/<widget_id>/data', methods = ['GET'])
def widget_data(user_id, widget_id):
    if user_id.isdigit():
        user_id = int(user_id)
    else:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    if widget_id.isdigit():
        widget_id = int(widget_id)
    else:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('users').get(user_id).run(g.conn)

    if cursor is None:
        return jsonify(
                    status = 400,
                    message = 'Bad Request: ',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('users').get(user_id)['widgets'].contains(lambda widget:
        widget['id'].eq(widget_id)
    ).run(g.conn)

    if not cursor:
        return jsonify(
                    status = 400,
                    message = 'Bad Request',
                    success = False,
                    data = None
                ), 400

    cursor = r.table('users').get(user_id)['widgets'].filter({
                    'id': widget_id
                }).run(g.conn)
    widgets = list(cursor)

    if len(widgets) != 1:
        return jsonify(
                status = 400,
                message = 'Bad Request',
                success = False,
                data = None
            ), 400

    data = get_data(widgets[0])

    if data is None:
        return jsonify(
                status = 400,
                message = 'Bad Request',
                success = False,
                data = None
            ), 400

    return jsonify(
            status = 200,
            message = 'OK',
            success = True,
            data = data
        ), 200
