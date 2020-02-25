from app import app
from flask import g
from rethinkdb import RethinkDB
from rethinkdb.errors import RqlRuntimeError
import sys

r = RethinkDB()

RDB_HOST = 'rethink'
RDB_PORT = 28015
RDB_NAME = 'dashboard'

def init_rethinkdb():
    connection = r.connect(host = RDB_HOST, port = RDB_PORT)
    try:
        r.db_create(RDB_NAME).run(connection)

        # Users
        r.db(RDB_NAME).table_create('users').run(connection)

        # Services
        r.db(RDB_NAME).table_create('services').run(connection)
        r.db(RDB_NAME).table('services').insert([
            {
                'id': 1,
                'name': 'Weather',
                'connections': []
            }, {
                'id': 2,
                'name': 'SoundCloud',
                'connections': []
            }, {
                'id': 3,
                'name': 'News',
                'connections': []
            }
        ]).run(connection)

        # Widgets
        r.db(RDB_NAME).table_create('widgets').run(connection)
        r.db(RDB_NAME).table('widgets').insert([
            {
                'id': 1,
                'service_id': 1,
                'name': 'Temperature',
                'description': 'View a city\'s temperature.',
                'type': 'widget-weather-light',
                'params': [
                    {'name': 'city_name', 'type': 'string'}
                ]
            }, {
                'id': 2,
                'service_id': 1,
                'name': 'Forecast',
                'description': 'View a city\'s forecast (pressure, humidity, wind, ...).',
                'type': 'widget-weather-big',
                'params': [
                    {'name': 'city_name', 'type': 'string'}
                ]
            }, {
                'id': 3,
                'service_id': 1,
                'name': 'Daytime',
                'description': 'View a city\'s daytime hours (sunrise and sunset).',
                'type': 'widget-weather-day',
                'params': [
                    {'name': 'city_name', 'type': 'string'}
                ]
            }, {
                'id': 4,
                'service_id': 2,
                'name': 'Profile',
                'description': 'View an artist\'s profile.',
                'type': 'widget-soundcloud-profile',
                'params': [
                    {'name': 'artist_username', 'type': 'string'}
                ]
            }, {
                'id': 5,
                'service_id': 2,
                'name': 'Top 15',
                'description': 'View the top 15 songs of a music genre in a specific country.',
                'type': 'widget-soundcloud-discover',
                'params': [
                    {'name': 'country_name', 'type': 'string'},
                    {'name': 'music_genre', 'type': 'string'}
                ]
            }, {
                'id': 6,
                'service_id': 2,
                'name': 'Artist popular tracks',
                'description': 'View an artist\'s most popular tracks.',
                'type': 'widget-soundcloud-top',
                'params': [
                    {'name': 'artist_username', 'type': 'string'}
                ]
            }, {
                'id': 7,
                'service_id': 3,
                'name': 'Topic',
                'description': 'View the latest articles written about a certain topic.',
                'type': 'widget-news-subject',
                'params': [
                    {'name': 'search_topic', 'type': 'string'}
                ]
            }, {
                'id': 8,
                'service_id': 3,
                'name': 'Region',
                'description': 'View the latest articles from a certain region and of a specific category.',
                'type': 'widget-news-region',
                'params': [
                    {'name': 'country_name', 'type': 'string'},
                    {'name': 'category_name', 'type': 'string'}
                ]
            }, {
                'id': 9,
                'service_id': 3,
                'name': 'Media source',
                'description': 'View the latest articles of a specific media source.',
                'type': 'widget-news-media',
                'params': [
                    {'name': 'media_source_name', 'type': 'string'}
                ]
            }
        ]).run(connection)

        print 'Database setup completed'
        sys.stdout.flush()
    except RqlRuntimeError:
        print 'Database already exists.'
        sys.stdout.flush()
    finally:
        connection.close()

init_rethinkdb()

@app.before_request
def before_request():
    try:
        g.conn = r.connect(host = RDB_HOST, port = RDB_PORT, db = RDB_NAME)
    except RqlDriverError:
        abort(503, "Database connection could be established.")

@app.teardown_request
def teardown_request(exception):
    try:
        g.conn.close()
    except AttributeError:
        pass
