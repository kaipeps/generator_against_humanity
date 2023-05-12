from flask import Blueprint
from controllers.cards_controller import browse, saved, create, delete, remove, generator

cards_routes = Blueprint('cards_routes', __name__)

cards_routes.route('/browse')(browse)
cards_routes.route('/user=<id>')(saved)
cards_routes.route('/user=<id>', methods = ['POST'])(create)
cards_routes.route('/<id>/delete', methods = ['POST'])(delete)
cards_routes.route('/user=<id>/<card_id>/remove', methods = ['POST'])(remove)
cards_routes.route('/generator/user=<id>')(generator)
