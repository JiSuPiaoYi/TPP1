import datetime

from app.ext import db




class Area(db.Model):
    area_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    parent_id = db.Column(db.Integer, index=True)
    pingyin = db.Column(db.String(100), nullable=False)
    key = db.Column(db.String(10))
    is_hot = db.Column(db.Boolean, default=False)

