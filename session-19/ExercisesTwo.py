# Exercise two
import http.client
import json
import termcolor

HOSTNAME = "www.metaweather.com"
ENDPOINT1 = "/api/location/search/?query="
ENDPOINT2 = "/api/location/"
METHOD = "GET"
headers = {'User-Agent': 'http-client'}

while True:
    City = input("What city are you interested in?: ")
    if len(City.split(" ")) > 1:
        lCity = City.split(" ")
        city = lCity[0]
    else: city = City
    try:
        conn = http.client.HTTPSConnection(HOSTNAME)
        conn.request(METHOD, ENDPOINT1 + city, None, headers)
        r1 = conn.getresponse()
        num = r1.read().decode("utf-8")
        conn.close()
        num = json.loads(num)
        if len(City.split(" ")) > 1:
            for elem in num:
                if elem.get("title").lower() == City.lower(): number = str(elem.get("woeid"))
            number = number
        elif len(num) > 1:
            termcolor.cprint("You have several options according to the city.", "white", end="\n")
            a = 1
            for elem in num:
                termcolor.cprint("{} {}".format(a, elem.get("title")), "white", end="\n")
                a +=1
            b = input("Please write the number of the option you want to choose: ")
            number = str(num[int(b)-1].get("woeid"))
        else: number = str(num[0].get("woeid"))
    except (UnicodeDecodeError, IndexError, NameError):
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

