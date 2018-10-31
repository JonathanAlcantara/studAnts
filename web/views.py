from json import loads

from flask import Blueprint
from flask import current_app
from flask import flash
from flask import jsonify
from flask import make_response
from flask import Markup
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

webs = Blueprint('webs',
                 __name__,
                 template_folder='templates',
                 static_folder='static'
                 )


@webs.route('/')
def hello():
    return "Hello World!"


@webs.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
