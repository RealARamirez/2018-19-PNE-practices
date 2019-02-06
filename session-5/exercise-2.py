def count_letter(arg1, arg2):
    n_characters = 0   # Counter for the characters
    for b in arg1:
        if b == arg2:
            n_characters += 1
    return n_characters

def count_bases(seq):
    return dict(zip(["A","C","G","T"],[count_letter(seq, "A"),count_letter(seq, "C"),count_letter(seq, "G"),count_letter(seq, "T")]))

# Main program
Sequence_one = input("Enter the sequence 1: ")
Sequence_two = input("Enter the sequence 2: ")
print("\nThe sequence 1 is {} bases in length".format(str(len(Sequence_one))))
print("Base A")
print("\tCounter: {}".format(str(count_bases(Sequence_one).get("A"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence_one).get("A")*100/len(Sequence_one),1)))))
print("Base T")
print("\tCounter: {}".format(str(count_bases(Sequence_one).get("T"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence_one).get("T")*100/len(Sequence_one),1)))))
print("Base C")
print("\tCounter: {}".format(str(count_bases(Sequence_one).get("C"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence_one).get("C")*100/len(Sequence_one),1)))))
print("Base G")
print("\tCounter: {}".format(str(count_bases(Sequence_one).get("G"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence_one).get("G")*100/len(Sequence_one),1)))))
print("\nThe sequence 2 is {} bases in length".format(str(len(Sequence_two))))
print("Base A")
print("\tCounter: {}".format(str(count_bases(Sequence_one).get("A"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence_two).get("A")*100/len(Sequence_two),1)))))
print("Base T")
print("\tCounter: {}".format(str(count_bases(Sequence_two).get("T"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence_two).get("T")*100/len(Sequence_two),1)))))
print("Base C")
print("\tCounter: {}".format(str(count_bases(Sequence_two).get("C"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence_two).get("C")*100/len(Sequence_two),1)))))
print("Base G")
print("\tCounter: {}".format(str(count_bases(Sequence_two).get("G"))))
print("\tPercentage: {}".format(str((round(count_bases(Sequence_two).get("G")*100/len(Sequence_two),1)))))