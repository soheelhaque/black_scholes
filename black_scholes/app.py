from __future__ import absolute_import
from flask import render_template
import connexion

import json
from flask import Response


# Create the application instance
APP = connexion.App(__name__, specification_dir='./openapi/')

# Read the swagger.yml file to configure the endpoints
APP.add_api('swagger.yml')

# Define and add a global error handler
def unhandled_exception(e):
    return Response(response=json.dumps({'error': str(e)}), status=400, mimetype="application/json")

APP.add_error_handler(Exception, unhandled_exception)


# Create a URL route in our application for "/"
@APP.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000, debug=True)
