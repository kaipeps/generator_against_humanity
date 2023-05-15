from flask import Blueprint
from controllers.generator_controller import new, result

generator_routes = Blueprint('generator_routes', __name__)

generator_routes.route('/new')(new)
generator_routes.route('', methods = ['POST'])(result)
