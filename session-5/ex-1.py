# Function designed for counting the number of an specific letter given in arg2, in a sequence given by arg1
def count_letter(arg1, arg2):
    n_characters = 0   # Counter for the characters
    for b in arg1:
        if b == arg2:
            n_characters += 1
    return n_characters

# Main program
s = "AGTACACTGGT"
na = count_letter(s, "A")
print("The number of the given letter is: {}".format(na))
# Calculate the length of the sequence
tl = len(s)
# Calculate the percent of of the given letter in the sequence
perc = round(100 * na/tl, 1)
# Print the total length of the sequence
print("The total length is: {}".format(tl))
# Print the percentage og the given letter in the sequence
print("The percentage of the given letter is: {}%".format(perc))