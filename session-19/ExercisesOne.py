# Exercise one

import http.client
import json
import termcolor
# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT1 = "/jokes/count"
ENDPOINT2 = "/categories"
ENDPOINT3 = "/jokes/random"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT1, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT2, None, headers)
r2 = conn.getresponse()
text_json_two = r2.read().decode("utf-8")
conn.close()

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT3, None, headers)
r3 = conn.getresponse()
text_json_three = r3.read().decode("utf-8")
conn.close()

# -- Generate the object from the json file
number = json.loads(text_json)
categories = json.loads(text_json_two)
random = json.loads(text_json_three)

termcolor.cprint("The number of jokes in the database are: {}.".format((number["value"])), "green", end="\n")
termcolor.cprint("The number of categories are {} and they are {}.".format(len(categories["value"]), "and".join(categories["value"])), "blue", end="\n")
termcolor.cprint("A random joke is: {}".format(random["value"]["joke"]), "red", end="\n")