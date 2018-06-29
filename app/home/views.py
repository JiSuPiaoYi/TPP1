from flask import Blueprint, jsonify
from sqlalchemy import func
import json

from app.cinemas.models import Movie
from app.ext import db
from app.home.models import Area
from app.utils.json_utils import to_list

home = Blueprint('home', __name__)

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


@home.route('/areas/')
def get_ares():
    result = {}
    # with_entities 过滤列
    # 相当于 db.session
    ares = {}
    try:
        for key in keys:
            # ares[key] = Area.query.with_entities(Area.name, Area.area_id).filter(Area.key == key).all()
            area_list = Area.query.filter(Area.key == key).all()
            if area_list:
                ares[key] = to_list(area_list)
        result.update(msg='success', status=200, ares=ares)
    except Exception as e:
        result.update(msg='查询失败', status=404)
    return jsonify(result)


# SELECT  COUNT(*) FROM MOVIE GROUP BY FLAG
@home.route('/moves/', methods=['GET', 'POST'])
def movies():
    result = {}
    try:
        movie = {}
        # 分组查出热门影片和热映的影片数量
        counts = Movie.query.with_entities(Movie.flag, func.count('*')).group_by(Movie.flag).all()
        # 查热门影片的前5部
        hot_movies = Movie.query.filter(Movie.flag == 1).limit(5).all()
        # 查询即将上映的前5部
        show_movies = Movie.query.filter(Movie.flag == 2).limit(5).all()

        movie.update(counts=counts, hot_movies=to_list(hot_movies), show_movies=to_list(hot_movies))
        result.update(status=200, msg='success', data=movie)
    except:
        result.update(status=404, msg='fail')
    return jsonify(result)


@home.route('/add/')
def add_json_data():
    with open(r'E:\Project\TPP\app\json\area.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        obj = data.get('returnValue')
        for key in keys:
            cities = obj.get(key)
            for city in cities:
                db.session.add(Area(name=city.get('regionName'),
                                    pingyin=city.get('pingYin'),
                                    parent_id=city.get('parentId'),
                                    area_id=city.get('cityCode'),
                                    key=key,
                                    ))
                db.session.commit()
    return 'success'
