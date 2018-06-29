from flask import Blueprint, request, jsonify
from sqlalchemy import distinct

from app.cinemas.models import Cinema, HallSchedule
from app.ext import db
from app.home.models import Movie
from app.movies.schema import movies_schema
from app.utils.json_utils import to_list

movies_blue = Blueprint('movies', __name__)

"""
参数flag
参数page
参数size

"""


# movie/list/?flag=1
@movies_blue.route('/list/')
def movie():
    result = {}
    try:
        # 判断是热门还是即将上映参数
        flag = request.values.get('flag', default=1, type=int)
        #  分页参数
        page = request.values.get('page', default=1, type=int)
        size = request.values.get('size', default=10, type=int)
        # 分页查询数据
        paginate = Movie.query.filter(Movie.flag == flag).paginate(page=page, per_page=size, error_out=False)
        """
        total 总条数
        pages 总页数
        items 数据
        """
        # 封装前端界面需要的数据
        pagination = {'total': paginate.total, 'pages': paginate.pages}
        # 要显示的主要数据
        movies = movies_schema.dump(paginate.items)
        # 组装返回的数据
        result.update(status=200, msg='success', data=movies.data, paginate=pagination)
    except:
        result.update(status=404, msg='fail')
    return jsonify(result)

'''
必要参数  城市名称和电影的id
'''

@movies_blue.route('/detail/')
def show_detail():
    result = {}
    try:
        # 获取电影的id
        mid = request.values.get('mid', type=int)
        # 获取所选择的城市
        city = request.values.get('city')
        # 获取影片详情信息
        movie = db.session.query(Movie.id, Movie.backgroundpicture, Movie.director).filter(Movie.mid == mid).first()
        # 通过城市查询地区的相关的信息
        districts = Cinema.query.with_entities(distinct(Cinema.district)).filter(Cinema.city == city).all()
        #    通过城市查询所有影院的信息
        cinemas = Cinema.query.order_by(Cinema.cid).filter(Cinema.city == city).all()
        # 通过电影的id和影院的id 就能查出所有的当前影院该影片的拍档情况
        hall_schedules = HallSchedule.query.filter(HallSchedule.cid == cinemas[0].cid).filter(
            HallSchedule.movie_id == mid).all()
        result.update(status=200, msg='success', movie=movie,
                      districts=districts, cinemas=to_list(cinemas)
                      , hall_schedule=to_list(hall_schedules))
    except Exception as e:
        result.update(status=404, msg='error')
    return jsonify(result)