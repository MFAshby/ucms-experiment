from http.server import HTTPServer,BaseHTTPRequestHandler,SimpleHTTPRequestHandler

class StaticHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="static", **kwargs)

def run(server_class=HTTPServer, handler_class=StaticHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
