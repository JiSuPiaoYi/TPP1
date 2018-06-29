from app.ext import ma
from app.cinemas.models import Cinema


class CinemaSchema(ma.ModelSchema):
    class Meta:
        model = Cinema


# 单个对象转化成字典
cinema_schema = CinemaSchema()
# 多个对象进行转化列表
cinemas_schema = CinemaSchema(many=True)
