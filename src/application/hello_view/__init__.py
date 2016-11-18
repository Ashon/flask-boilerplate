
from flask import Blueprint

from application.hello_view.views import HelloView


def get_blueprint():
    ''' get_blueprint() should returns flask.Blueprint
    '''

    # Register the urls
    blueprint = Blueprint('hello_view', __name__)
    blueprint.add_url_rule('/', view_func=HelloView.as_view('hello_view'))

    return blueprint
