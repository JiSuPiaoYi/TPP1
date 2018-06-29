import datetime

from app.ext import db

# 影院
class Cinema(db.Model):
    __tablename__ = 'cinemas'
    mid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    city = db.Column(db.String(10))
    district = db.Column(db.String(10))
    address = db.Column(db.String(64))
    phone = db.Column(db.String(20))
    score = db.Column(db.Float(3, 1), default=10.0)
    hallnum = db.Column(db.Integer)
    servicecharge = db.Column(db.Float(3, 1), default=1.2)
    astrict = db.Column(db.Integer)
    flag = db.Column(db.Boolean, default=True)
    is_delete = db.Column(db.Boolean, default=False)



# 影厅表
class Hall(db.Model):
    hid = db.Column(db.Integer, primary_key=True)
    # 设置外键 向关联影院
    mid = db.Column(db.Integer, db.ForeignKey('cinemas.mid'))
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    seats = db.Column(db.Integer, default=0)  # 座位数
    is_delete = db.Column(db.Boolean, default=False)


# 档期表
class HallSchedule(db.Model):
    hsid = db.Column(db.Integer, primary_key=True)
    original_price = db.Column(db.Numeric(6, 2))    # 原价
    dis_price = db.Column(db.Numeric(6, 2))    # 折扣价
    start_time = db.Column(db.DateTime)
    starus = db.Column(db.Integer, default=1)
    is_delete = db.Column(db.Boolean, default=False)
    # 关联外键  电影、影厅、影院
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.mid'))
    hid = db.Column(db.Integer, db.ForeignKey('hall.hid'))
    cid = db.Column(db.Integer, db.ForeignKey('cinemas.mid'))


# 电影
class Movie(db.Model):
    __tablename__ = 'movies'
    cid = db.Column('mid', db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    showname = db.Column(db.String(64), unique=True, nullable=False, index=True)
    shownameen = db.Column(db.String(64), nullable=False, index=True)
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(64))
    type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer)
    screeningmodel = db.Column(db.String(10))
    openday = db.Column(db.DateTime, default=datetime.datetime.now())
    backgroundpicture = db.Column(db.String(64))
    flag = db.Column(db.Boolean, default=True)
    is_delete = db.Column(db.Boolean, default=False)


