from flask_caching import Cache
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def init_ext(app):
    # 数据库初始化
    init_db(app)
    # 发送邮件初始化
    init_mail(app)
    # 缓存配置初始化
    init_cache_config(app)

# 配置数据库orm框架
db = SQLAlchemy()
migrate = Migrate()



# 初始化数据库配置
def init_db(app):
    db.init_app(app=app)
    migrate.init_app(app, db)



# 邮箱的配置
mail = Mail()

def init_mail(app):
    mail.init_app(app)


# 配置缓存
'''
1.flask-caching
2.redis
'''
cache = Cache(config={'CACHE_TYPE':'redis'})

def init_cache_config(app):
    cache.init_app(app)


# 模型转化
ma = Marshmallow()


def init_marshmallow(app):
    ma.init_app(app)
