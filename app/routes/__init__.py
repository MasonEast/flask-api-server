from .user import user_ns

def register_namespaces(api):
    api.add_namespace(user_ns, path='/user')