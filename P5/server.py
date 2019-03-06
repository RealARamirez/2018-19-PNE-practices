import http.server
import socketserver

# Define the port
PORT = 8000

# Create a type of object TestHandler that inherit functions from http.server.BaseHTTPRequestHandler
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET received")
        print("Request line" + self.requestline)
        print("       Cmd:  " + self.command)
        print("      Path:  " + self.path)


        if self.path == "/":
            file = open("index.html", "r")
            content = file.read()
            file.close()
        elif self.path == "/blue/":
            file = open("blue.html", "r")
            content = file.read()
            file.close()
        elif self.path == "/pink/":
            file = open("pink.html", "r")
            content = file.read()
            file.close()
        else:
            file = open("error.html", "r")
            content = file.read()
            file.close()
        self.send_response(200);
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))
        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as Svr:
    Svr.serve_forever()