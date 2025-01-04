import os
import tempfile
import logging
from flask import Flask
from routes.routes import generate_content_route, index_route


app = Flask(__name__, static_folder='public')

generate_content_route(app)
index_route(app)


UPLOAD_FOLDER = tempfile.mkdtemp()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
