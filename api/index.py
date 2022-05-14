from http.server import BaseHTTPRequestHandler
from urllib import parse
import numpy as np


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        a = str(np.random.choice([1, 2, 3, 4, 5, 6]))
        if 'name' in dic:
            message = 'Hello, ' + dic["name"] + '!'
        else:
            message = f'Hello, stranger! {a}'
            self.wfile.write(message.encode())
        return
