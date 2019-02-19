import socket

# SERVER IP, PORT
IP = "212.128.253.98"
PORT = 8083


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    msg = input("Write down the message tou want to send: ")

    if msg == "":
        break

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(9999).decode()

    # Print the server's response
    print("Response: {}".format(response))

s.close()