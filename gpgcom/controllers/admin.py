from flask import Blueprint
from flask_spirits import jsonify

from gpgcom.models import Game


bp = Blueprint('admin', __name__)
