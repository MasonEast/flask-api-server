import jwt
from datetime import timedelta
import os

from flask_restx import Namespace, Resource, fields
from flask import request

from app.models import Article
from utils import Times
from utils.decorator import token_required

from config import Config

article_ns = Namespace('article', description='文章')

article_model = article_ns.model('article_model', {
    'title': fields.String(required=False, description='标题'),
    'author': fields.String(required=False, description='作者'),
    'text': fields.String(required=True, description='内容'),
    'tags': fields.String(required=True, description='标签'),
    'create_time': fields.String(required=False, description='创建时间'),

    'views': fields.Integer(required=False, description='浏览量'),
    'likes': fields.Integer(required=False, description='点赞量'),
    'collects': fields.Integer(required=False, description='收藏量'),
    'transmits': fields.Integer(required=False, description='转发量'),
})

login_modal = article_ns.model('login_modal', {
    'username': fields.String(required=True, description='账号'), # 使用邮箱或手机号替代用户名做登录
    'password': fields.String(required=True, description='密码'),
})

@article_ns.route('/create')
class Create(Resource):

    @article_ns.expect(article_model, validate=True)
    @token_required
    def post(self, current_user):
        try:
            data = request.json

            now = Times.now()
            data['create_time'] = now
            data['author'] = self.toJSON()['nickname']
            data['views'] = 1
            data['likes'] = 0
            data['collects'] = 0
            data['transmits'] = 0

            new_article = Article(**data)

            new_article.save()

            return {"success": True,
                "msg": "发布成功"}, 200
    
        except Exception as err:
            new_article.rollback()
            return {"error": f"Error: {err}"}, 500

@article_ns.route('/<int:id>')
@article_ns.param('id', 'The article identifier')
class ArticleDetail(Resource):
    @article_ns.marshal_with(article_model)

    def get(self, id):

        detail = Article.get_by_id(id)
        
        return detail, 201
            

   