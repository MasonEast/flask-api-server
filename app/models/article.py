
from . import db

from utils import HashBcrypt

# id，标题，时间，作者，标签，内容，浏览量，点赞量，收藏量，转发量，评论

class Article(db.Model):
    article_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False) # 内容
    tags = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.String(100), nullable=False)

    
    views = db.Column(db.Integer, nullable=False) # 浏览量
    likes = db.Column(db.Integer, nullable=False) # 点赞量
    collects = db.Column(db.Integer, nullable=False) # 收藏量
    transmits = db.Column(db.Integer, nullable=False) # 转发量

    def save(self):
        db.session.add(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    def check_password(self, password):
        return HashBcrypt.check(password, self.password)
    
    def set_status(self, status):
        self.status = status

    def toJSON(self):

        cls_dict = {}
        cls_dict['_id'] = self.article_id
        cls_dict['phone'] = self.phone
        cls_dict['email'] = self.email

        return cls_dict

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def get_by_phone(cls, phone):
        return cls.query.filter_by(phone=phone).first()

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer) # 关联文章
    author = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False) # 内容
    create_time = db.Column(db.String(100), nullable=False)

    
    views = db.Column(db.Integer, nullable=True) # 浏览量
    likes = db.Column(db.Integer, nullable=True) # 点赞量
    collects = db.Column(db.Integer, nullable=True) # 收藏量
    transmits = db.Column(db.Integer, nullable=True) # 转发量

    def save(self):
        db.session.add(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    def check_password(self, password):
        return HashBcrypt.check(password, self.password)
    
    def set_status(self, status):
        self.status = status

    def toJSON(self):

        cls_dict = {}
        cls_dict['_id'] = self.article_id
        cls_dict['phone'] = self.phone
        cls_dict['email'] = self.email

        return cls_dict

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def get_by_phone(cls, phone):
        return cls.query.filter_by(phone=phone).first()
