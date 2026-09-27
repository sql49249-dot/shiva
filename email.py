from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q=parse_qs(urlparse(self.path).query)
        key=q.get("key",[None])[0]
        email=q.get("email",[None])[0]
        out={"status":"ok","type":"test","email":email,
             "data":{"name":"TEST USER","mobile":"9999999999",
                     "aadhaar":"000000000000","city":"TEST CITY"}}
        if key!="KING8090":
            out={"error":"Invalid API key"}
            code=401
        elif not email:
            out={"error":"email is required"}
            code=400
        else:
            code=200
        self.send_response(code)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(out).encode())
