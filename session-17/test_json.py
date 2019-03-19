import json
import termcolor

f = open("person.json", "r")

person = json.load(f)

print()

def array_wk(array):
    for i,num in enumerate(array):
        termcolor.cprint("  Phone", "blue", end=" ")
        print(i)
        termcolor.cprint("      Type:", "red", end=" ")
        print(num["type"])
        termcolor.cprint("      Number:", "red", end=" ")
        print(num["number"])
    return
#Main
print("Total people in the database {}\n".format(len(person["people"])))
for elem in person["people"]:
    termcolor.cprint("Name: ", "green", end=" ")
    print(elem["Firstname"], elem["Lastname"])
    termcolor.cprint("Age: ", "green", end=" ")
    print(elem["age"])
    termcolor.cprint("Number of phones: ", "green", end=" ")
    print(len(elem["phoneNumber"]))
    array_wk(elem["phoneNumber"])