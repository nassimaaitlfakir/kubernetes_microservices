from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with urlopen(os.environ["SERVICE_C_URL"]) as response:
            data = response.read()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)

HTTPServer(("0.0.0.0", 8082), Handler).serve_forever()