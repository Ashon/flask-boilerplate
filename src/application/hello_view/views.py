
from flask import jsonify
from flask.views import MethodView


class HelloView(MethodView):

    def get(self):
        response = {
            'message': 'hello'
        }

        return jsonify(response)
