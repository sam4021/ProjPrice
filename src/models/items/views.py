from flask import Blueprint

item_blueprint = Blueprint('items', __name__)

@item_blueprint.route('/item/<string:name>')
def item_page(name):
    pass

@item_blueprint.route('/load')
def load_item():
    '''
    loads an item's data using their store and return a JSON representation of it
    :return: 
    '''