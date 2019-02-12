# Example of reading a file located in our local file system

Name = "mynotes.txt"

# Open the file
myfile = open(Name, 'r')

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

myfile.close()

f = open(Name, "a")
f.write("\nTHIS IS A TEXT EXAMPLE FOR ADDING TO MY FILE")
f.close()
print("The end.")
