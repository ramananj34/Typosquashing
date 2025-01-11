from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json

HOST = "192.168.0.35"
PORT = 8000

class TyposquatServer(BaseHTTPRequestHandler):
    def do_GET(self):
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        test_url = params.get('url', [None])[0]
        response = {
            "url-answer": test_url
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
        

server = HTTPServer((HOST, PORT), TyposquatServer)
print("Server is up")
try: 
    server.serve_forever()
except KeyboardInterrupt:
    print("Shutting down server")
    pass
server.server_close()
print("Server is down")