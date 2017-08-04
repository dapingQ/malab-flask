from flask import Blueprint

main = Blueprint('main', __name__)

from . import routing, forms, static_routing
