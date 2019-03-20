# -- Example of a client that uses the HTTP.client library
# -- for requesting a JSON object and printing their
# -- contents
import http.client
import json
import termcolor
from Seq import Seq

PORT = 80
SERVER = "rest.ensembl.org"

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

sequence = json.loads(data1)
Frat1 = Seq(sequence["seq"])

termcolor.cprint("In Frat1 gene there are {} bases, and {} of them are T bases.".format(Frat1.len(), Frat1.count("T")), "blue", end="\n")
Bases = {"A", "G", "C", "T"}
NumBases = 0
for elem in Bases:
    if Frat1.count(elem) > NumBases: NumBases, PopularBase = Frat1.count(elem), elem
termcolor.cprint("The most popular base is {} and its percentage is {}%".format(PopularBase, Frat1.perc(PopularBase)), "green", end="\n")
termcolor.cprint("The percentage of all bases are the following:", "red", end=" ")
for elem in Bases: termcolor.cprint("the base {} has a percentage of {}%,".format(elem, Frat1.perc(elem)), "red", end=" ")
termcolor.cprint("with a total of 100%.", "red")