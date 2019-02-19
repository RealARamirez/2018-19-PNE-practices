import socket

# Configure the IP and the Port of the server
PORT = 8083
IP =  "212.128.253.98"
MAX_OPEN_REQUEST = 5

# Definition for attending the client
# 9999 is the max length
# utf-8 is readable format
def process_client(cs):
    msg = cs.recv(9999).decode("utf-8")
    print("Message for the client: {}".format(msg))
    # Sending the message back to the client
    cs.send(str.encode(msg))

# Create the socket, that connect to internet and that is STREAM
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attach (Bind) the socket to the IP and to the port
serversocket.bind((IP, PORT))

# Start listening from the client, number of maximum request
serversocket.listen(MAX_OPEN_REQUEST)

# Print out some information
print("Socket ready: {}".format(serversocket))

while True:
    # Make the server wait for connection
    print("Waiting for connections at: {}".format(IP, PORT))

    # Wait until a client is connected and return the IP address of the client and the client socket
    (clientsocket, address) = serversocket.accept()

    # - - - Process the client request
    print("Attending client; {}".format((address)))

    # Atending a client
    process_client(clientsocket)



    # Close the socket
    clientsocket.close()

