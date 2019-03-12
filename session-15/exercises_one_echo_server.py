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
        if self.requestline == "GET / HTTP/1.1" or self.requestline == "GET /echo HTTP/1.1" or self.requestline == "GET /echo/ HTTP/1.1":
            file = open("exercises_one_echo_server.html", "r")
            content = file.read()
            file.close()
        elif self.requestline.startswith("GET /echo?msg="):
            message = self.requestline.split(" ")[1]
            message = message[10:]
            content = """
            <!DOCTYPE html>
            <html lang="en" dir="ltr">
                <head>
                    <meta charset="utf-8">
                    <title>Echo</title>
                </head>
                    <body>
                        <h1>ECO del mensaje recibido</h1>
                        <p>{}</p>
                        <a href="/">Link a la page principal</a>
                    </body>
            </html>
            """.format(message)
        else:
            file = open("error.html", "r")
            content = file.read()
            file.close()
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

