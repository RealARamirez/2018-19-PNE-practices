# -- Example of a client that uses the HTTP.client library
# -- for requesting a JSON object and printing their
# -- contents
import http.client
import json
import termcolor

PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

def array_wk(array):
    for i,num in enumerate(array):
        termcolor.cprint("  Phone {}:".format(i), "blue", end="\n")
        termcolor.cprint("      Type:", "red", end=" ")
        print(num["type"])
        termcolor.cprint("      Number:", "red", end=" ")
        print(num["number"])
    return

# Main
print("Total people in the database {}\n".format(len(person["people"])))

for elem in person["people"]:
    termcolor.cprint("Name: ", "green", end=" ")
    print(elem["Firstname"], elem["Lastname"])
    termcolor.cprint("Age: ", "green", end=" ")
    print(elem["age"])
    termcolor.cprint("Number of phones: ", "green", end=" ")
    print(len(elem["phoneNumber"]))
    array_wk(elem["phoneNumber"])
    print("\n")
