# Program for the client
import socket
from Seq import Seq
# Socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Configure the port and the IP
PORT = 8080
IP = "212.128.253.101"
# Create connection
s.connect((IP, PORT))
# Create the loop
while True:
    # Message that send (the sequence)
    Message = input("Type the sequence you will work with: ")
    # Create an stop statement when the sequence in empty
    if Message == "":
        print("Empty sequence, program ended.")
        s.close()
        break
    # Make the sequence an object of type Seq
    S1 = Seq(Message)
    # Classify as Seq S1 reverse
    S2 = Seq(S1.reverse())
    # Classify as Seq S2 complement
    S3 = Seq(S2.complement())
    # Send S3 encoding its string as bites
    s.send(str.encode(S3.strbases))

