"""



"""


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
        if 'name' in dic:
            b = dic['name']
            print(b)
            message = f'Hello "{b}"!'
        else:
            a = np.random.choice([1, 2, 3, 4, 5, 6])
            print(a)
            message = f'Hello "{a}" stranger!'

        self.wfile.write(message.encode())
        return 0
