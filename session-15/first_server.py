import http.server
import socketserver
import termcolor

# Define the port
PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET received")
        termcolor.cprint(self.requestline, "green")
        print("       Cmd:  " + self.command)
        print("      Path:  " + self.path)
        file = open("index.html", "r")
        content = file.read()
        file.close()
        path = self.path
        message = path.lstrip("/echo?msg=")
        print(message)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))
        return


Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as Svr:
    print("Serving at Port: {}".format(PORT))
    try:
        Svr.serve_forever()
    except KeyboardInterrupt:
        print("Program stopped")
        Svr.server_close()


print("The server is stopped")
