from flask import Blueprint
from controllers.cards_controller import saved, new, create, edit, update, delete, remove, browse, save

cards_routes = Blueprint('cards_routes', __name__)

cards_routes.route('/saved/<user_id>')(saved)
cards_routes.route('/new')(new)
cards_routes.route('/create/<user_id>', methods = ['POST'])(create)
cards_routes.route('/edit/<card_id>')(edit)
cards_routes.route('/update/<card_id>', methods = ['POST'])(update)
cards_routes.route('/delete/<card_id>', methods = ['POST'])(delete)
cards_routes.route('/remove/<card_id>-<user_id>', methods = ['POST'])(remove)
cards_routes.route('/browse')(browse)
cards_routes.route('/save/<card_id>')(save)
