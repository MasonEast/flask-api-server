from .user import user_ns

def register_namespace(api):
    api.add_namespace(user_ns, path='/user')