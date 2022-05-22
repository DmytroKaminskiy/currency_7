def hello():
    return b'HELLO\n'

def world():
    return b'WORLD\n'


urlpatterns = {
    '/world': world,
    '/hello': hello,
}

########################################

def application(environ, start_response):

    path = environ['PATH_INFO']
    view_func = urlpatterns.get(path)
    if view_func:
        data = view_func()
    else:
        data = b"Not Found\n"

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
