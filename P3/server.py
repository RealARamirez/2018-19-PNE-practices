import socket
from request import request

# Configure the IP
IP = "212.128.253.99"

# Configure the port
PORT = 8080

# Configure the maximum of open request
MAX_OPEN_REQUEST = 5

# Create a socket that connect to the internet of type STREAM
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind it to the IP and to the PORT
s_socket.bind((IP, PORT))

# Make the socket start listening
s_socket.listen(MAX_OPEN_REQUEST)

# Create a loop for making the server work correctly
while True:
    # Accept the connections
    (cl_socket, address) = s_socket.accept()

    # Receive messages from the client and attach it to the variable message
    message = cl_socket.recv(2048).decode("utf-8")
    print(message)

    # Make the message be an object of type request
    message = request(message)

    # Main functions
    # With a message of type request we can develop the program functionality

    # If the request intentionality is to check if the server is working, else it should develop all operations
    if message.alive_checker() == "ALIVE":
        # Send the message to the client
        cl_socket.send(str.encode(message.alive_checker()))
    # Check if the sequence is correctly typed
    elif message.seq_checker() == "ERROR":
        # Send it as a message for the client
        cl_socket.send(str.encode(message.seq_checker()))
    # Function for normal messages
    else:
        # Send the resolution of the request operations
        cl_socket.send(str.encode(message.main_function()))

    # Close the socket
    cl_socket.close()