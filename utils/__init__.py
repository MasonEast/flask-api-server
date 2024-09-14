import bcrypt
from datetime import datetime

import re
import os


class Valid():
    def valid_email(email):
        # 定义匹配邮箱格式的正则表达式
        email_pattern = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        # 使用正则表达式进行匹配
        return re.match(email_pattern, email)
    
    def valid_phone(phone):
        # 定义匹配中国大陆手机号格式的正则表达式
        phone_pattern = re.compile(r"^1[3-9]\d{9}$")
        # 使用正则表达式进行匹配
        return re.match(phone_pattern, phone)


class HashBcrypt():

    @staticmethod
    def hash(password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    
    @staticmethod
    def check(password, password_hash):

        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    
class Times():

    def now():
        return datetime.now().timestamp()
    
    def nowUTC():
        return datetime.utcnow()

def create_upload_dir(directory):
    
    if os.path.exists(directory): 
        return
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' created successfully")
    except OSError as error:
        print(f"Error creating directory '{directory}': {error}")

