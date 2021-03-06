import http.server
import socketserver
import termcolor
from Seq import Seq

# Define the port
PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET received")
        termcolor.cprint(self.requestline, "green")
        print("       Cmd:  " + self.command)
        print("      Path:  " + self.path)
        if self.requestline == "GET / HTTP/1.1" or self.requestline == "GET /seq HTTP/1.1":
            file = open("main_page.html", "r")
            content = file.read()
            file.close()
        elif self.requestline.startswith("GET /echo?"):
            request = self.requestline.split(" ")[1]
            request = request.split("&")
            sequence = Seq(request[0][10:])
            if sequence.checker():
                message = "The sequence given is: {}, ".format(sequence)
                for a in range(len(request)):
                    if request[a].startswith("len"): message += "its length is {}, ".format(sequence.len())
                    elif request[a].endswith("count"): message += "and the operation count on the {} base is {}. ".format(request[a+1][-1], sequence.count(request[a+1][-1]))
                    elif request[a].endswith("perc"): message += "and the operation percentage on the {} base is {}%.".format(request[a+1][-1], sequence.perc(request[a+1][-1]))
                content = """
                        <!DOCTYPE html>
                        <html lang="en" dir="ltr">
                            <head>
                                <meta charset="utf-8">
                                <title>Sequence operations</title>
                            </head>
                                <body>
                                    <h1>Sequence operations</h1>
                                    <p>{}</p>
                                    <a href="/">Link a la page principal</a>
                                </body>
                        </html>
                        """.format(message)
            else:
                file = open("error_message.html", "r")
                content = file.read()
                file.close()
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
