from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q=parse_qs(urlparse(self.path).query)
        key=q.get("key",[None])[0]
        value=q.get("aadhaar",q.get("aadhar",[None]))[0]
        out={"status":"ok","type":"test","aadhaar":value,
             "data":{"name":"TEST USER","mobile":"9999999999",
                     "email":"test@example.com","city":"TEST CITY"}}
        if key!="KING8090":
            out={"error":"Invalid API key"}
            code=401
        elif not value:
            out={"error":"aadhaar is required"}
            code=400
        else:
            code=200
        self.send_response(code)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(out).encode())
