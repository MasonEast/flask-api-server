import os

class Config:
    # 基本配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'

    # 使用 PyMySQL 驱动
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Ljf941118@localhost:3306/flask-db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # token过期时间
    EXPIRE_MINUTES = 30