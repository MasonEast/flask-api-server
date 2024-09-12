
from . import db

from utils import HashBcrypt

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(20), nullable=True)
    avatar_url = db.Column(db.String(255), nullable=True)
    intro = db.Column(db.Text, nullable=True) # 简介
    birthday = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(10), nullable=True) # 性别

    status = db.Column(db.Integer, nullable=False) # 状态 1 在线， 0 离线
    create_time = db.Column(db.String(100), nullable=False)
    last_login_time = db.Column(db.String(100), nullable=False)

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
        cls_dict['_id'] = self.user_id
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
