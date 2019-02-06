def count_letter(arg1, arg2):
    n_characters = 0   # Counter for the characters
    for b in arg1:
        if b == arg2:
            n_characters += 1
    return n_characters

def count_bases(seq):
    return dict(zip(["A","C","G","T"],[count_letter(seq, "A"),count_letter(seq, "C"),count_letter(seq, "G"),count_letter(seq, "T")]))

# Main program
Sequence = input("Enter the sequence: ")
print("The sequence is {} bases in length".format(str(len(Sequence))))
print("Base A")
print("\tCounter: {}".format(str(count_bases(Sequence).get("A"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence).get("A")*100/len(Sequence),1)))))
print("Base T")
print("\tCounter: {}".format(str(count_bases(Sequence).get("T"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence).get("T")*100/len(Sequence),1)))))
print("Base C")
print("\tCounter: {}".format(str(count_bases(Sequence).get("C"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence).get("C")*100/len(Sequence),1)))))
print("Base G")
print("\tCounter: {}".format(str(count_bases(Sequence).get("G"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence).get("G")*100/len(Sequence),1)))))

