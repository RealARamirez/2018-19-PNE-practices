import socket
import termcolor

# SERVER IP, PORT
IP = "212.128.253.98"
PORT = 8080


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    msg = input("Write down the message tou want to send: ")


    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))


    if msg == "EXIT":
        break

    # Receive the servers respoinse
    response = s.recv(9999).decode()

    # Print the server's response
    print(termcolor.cprint("Response: {}".format(response), "green"))

    s.close()