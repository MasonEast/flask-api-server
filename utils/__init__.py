import bcrypt
from datetime import datetime

class HashBcrypt():
    def hash(self):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(self.encode('utf-8'), salt)
    def check(self, hash):
        return self == bcrypt.checkpw(hash)
    
class Times():

    def now():
        return datetime.now().timestamp()
