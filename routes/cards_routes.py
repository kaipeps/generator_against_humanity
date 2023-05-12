from flask import Blueprint
from controllers.cards_controller import index, browse, saved, create, generator

cards_routes = Blueprint('cards_routes', __name__)

cards_routes.route('')(index)
cards_routes.route('')(browse)
cards_routes.route('/user=<id>')(saved)
cards_routes.route('/user=<id>', methods = ['POST'])(create)
cards_routes.route('')(generator)
