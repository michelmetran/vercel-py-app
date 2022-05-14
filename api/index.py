import numpy as np
from urllib import parse
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        a = str(np.random.choice([1, 2, 3, 4, 5, 6]))
        b = dic["name"]
        if 'name' in dic:
            message = f'Hello, {b}!'
        else:
            message = f'Hello "{a}" stranger!'
            self.wfile.write(message.encode())
        return
