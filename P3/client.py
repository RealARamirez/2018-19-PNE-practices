import socket

# Configure the IP
IP = "212.128.253.99"

# Configure the port
PORT = 8080

while True:
    # Print a message that show how the client works
    print("Welcome to the program for working with sequences.\nType an empty input for knowing if the server is alive.\nOtherwise, type firstly a sequence, intro and separate with intro the propierties of the sequence, with an empty input you will send the message.")

    # Create a message for sending to the client
    message = "\n"

    # Create a loop that add the successive inputs
    while True:
        inp = input("> ")
        message.join(inp)
        if inp == "":
            break

    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection
    s.connect((IP, PORT))

    # Send the message to the server
    s.send(str.encode(message))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Close the socket
    s.close()
