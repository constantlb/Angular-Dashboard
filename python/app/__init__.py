from flask import Flask, jsonify
from flask_cors import CORS
from routes.misc import api as misc_bp
from routes.services import api as services_bp
from routes.users import api as users_bp
from routes.widgets import api as widgets_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(misc_bp)
app.register_blueprint(services_bp, url_prefix = '/services')
app.register_blueprint(users_bp, url_prefix = '/users')
app.register_blueprint(widgets_bp, url_prefix = '/widgets')

@app.errorhandler(400)
def bad_request(e):
    return jsonify(
        status = 400,
        message = 'Bad Request',
        success = False,
        data = None
    ), 400

@app.errorhandler(403)
def forbidden(e):
    return jsonify(
        status = 403,
        message = 'Forbidden',
        success = False,
        data = None
    ), 403

@app.errorhandler(404)
def not_found(e):
    return jsonify(
        status = 404,
        message = 'Not Found',
        success = False,
        data = None
    ), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(
        status = 405,
        message = 'Method Not Allowed',
        success = False,
        data = None
    ), 405

from app import rethink
