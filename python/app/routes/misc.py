from flask import Blueprint, jsonify, g, request
from rethinkdb import RethinkDB
import datetime
import time

r = RethinkDB()
api = Blueprint('misc', __name__)

@api.route('/about', methods = ['GET'])
def about():
    cursor = r.db('dashboard').table('services').merge(lambda service:
                    { 'widgets': r.db('dashboard').table('widgets').filter({'service_id': service['id']}).order_by('id').without('id', 'service_id').coerce_to('array') }
                ).order_by('id').without('connections', 'id').run(g.conn)
    services = list(cursor)

    about = {
        'client': {
            'host': request.remote_addr
        },
        'server': {
            'current_time': time.mktime(datetime.datetime.now().timetuple()),
            'services': services
        }
    }

    return jsonify(about), 200
