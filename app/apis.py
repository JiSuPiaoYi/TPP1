from flask import Blueprint


# 注册蓝图

from app.cinemas.views import cinema_blue
from app.home.views import home
from app.user.views import user

def register_blue(app):
    # app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(cinema_blue, url_prefix='/cinema')