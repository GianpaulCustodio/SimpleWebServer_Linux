import socketserver
import http.server
server = socketserver.TCPServer(('0.0.0.0',3000), http.server.SimpleHTTPRequestHandler)
print('Started webserver at port 3000')
server.serve_forever()
