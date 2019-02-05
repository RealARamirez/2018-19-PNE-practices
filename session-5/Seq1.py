class Seq:   # A class for representing sequences
    def __init__(self, strbases):
        print("New empty sequence created!")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq
        All the objects of Class Gene will
        inheritage the methods from Seq class"""
    pass


s1 = Gene("ATTCGATC")
s2 = Seq("AAACCT")


l1 = s1.len()
l2 = s2.len()

str1 = s1.strbases
str2 = s2.strbases
print("Sequence1: {}".format(str1))
print(" Length: {}".format(l1))
print("Sequence2: {}".format(str2))
print(" Length: {}".format(l2))
print("the end")
