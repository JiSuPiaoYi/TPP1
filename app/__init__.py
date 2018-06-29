from flask import Flask
from flask_cors import CORS

from app import settings
from app.apis import register_blue
from app.ext import init_ext
from app.settings import env

app = Flask(__name__)
app.debug = True
CORS(app, supports_credentials=True)

def create_app(evn_name):
    app.config.from_object(env.get(evn_name))
    register_blue(app)
    init_ext(app)
    return app