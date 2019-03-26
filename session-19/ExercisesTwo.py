# Exercise two
import http.client
import json
import termcolor

HOSTNAME = "www.metaweather.com"
ENDPOINT1 = "/api/location/search/?query="
ENDPOINT2 = "/api/location/"
METHOD = "GET"

while True:
    City = input("What city are you interested in?: ")
    headers = {'User-Agent': 'http-client'}
    try:
        conn = http.client.HTTPSConnection(HOSTNAME)
        conn.request(METHOD, ENDPOINT1 + City, None, headers)
        r1 = conn.getresponse()
        num = r1.read().decode("utf-8")
        conn.close()
        num = json.loads(num)
        if num[0].get("title") != City:
            print("It is not a valid city")
            break
        if len(num) != 1:
            print("It is not a valid city")
            break
        number = str(num[0].get("woeid"))
    except (UnicodeDecodeError, IndexError):
        print("It is not a valid city")
        break
    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request(METHOD, ENDPOINT2 + number + "/", None, headers)
    r2 = conn.getresponse()
    data = r2.read().decode("utf-8")
    data = json.loads(data)
    CT = data["consolidated_weather"][0]['weather_state_name']
    termcolor.cprint("Temperature:", "blue", end=" ")
    temperature = data["consolidated_weather"][0]["the_temp"]
    termcolor.cprint(temperature, "white", end="\n")
    termcolor.cprint("Sunset:", "blue", end=" ")
    termcolor.cprint(CT, "white", end="\n")
    break

