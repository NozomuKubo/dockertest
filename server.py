import http.server
import socketserver

PORT = 8888

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Instruction server from docekr) this is Nozomu. port", PORT)
    httpd.serve_forever()
