

from .user import user_ns
from .article import article_ns

def register_namespaces(api):
    api.add_namespace(user_ns, path='/user')
    api.add_namespace(article_ns, path='/article')

