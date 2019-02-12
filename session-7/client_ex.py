# Programming our first client

import socket

while True:
    Chat = input("What do you want to send?: ")
    if Chat == "End":
        break
    # Socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket created")

    PORT = 8080
    IP = "212.128.253.64"

    s.connect((IP, PORT))

    s.send(str.encode(Chat))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER")
    print(msg)


    s.close()

    print("The end")

