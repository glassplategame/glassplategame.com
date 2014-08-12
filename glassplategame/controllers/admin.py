from flask import Blueprint
from flask_spirits import jsonify

from glassplategame.models import Game


bp = Blueprint('admin', __name__)
