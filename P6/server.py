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
