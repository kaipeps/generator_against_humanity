from flask import Blueprint
from controllers.cards_controller import browse, saved, create, edit, delete, remove, generator

cards_routes = Blueprint('cards_routes', __name__)

cards_routes.route('/browse')(browse)
cards_routes.route('/saved/<user_id>')(saved)
cards_routes.route('/create/<user_id>', methods = ['POST'])(create)
cards_routes.route('/edit/<card_id>', methods = ['POST'])(edit)
cards_routes.route('/delete/<card_id>', methods = ['POST'])(delete)
cards_routes.route('/remove/<user_id>/<card_id>', methods = ['POST'])(remove)
cards_routes.route('/generator')(generator)
