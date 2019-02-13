# Program for the client
import socket
from Seq import Seq
# Configure the port and the IP
PORT = 8080
IP = "212.128.253.101"
# Create the loop
while True:
    # Socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Create connection
    s.connect((IP, PORT))
    # Message that send (the sequence)
    Message = input("Type the sequence you will work with: ")
    # Create an stop statement when the sequence in empty
    if Message == "":
        print("Empty sequence, program ended.")
        s.close()
        break
    # Send S3 encoding its string as bites
    s.send(str.encode(Message))
    # Print the message back
    print(s.recv(2048).decode("utf-8"))
    # Close the server
    s.close()

