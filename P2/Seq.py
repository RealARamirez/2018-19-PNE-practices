def count_letter(arg1, arg2):
    n_characters = 0   # Counter for the characters
    for b in arg1:
        if b == arg2:
            n_characters += 1
    return n_characters

class Seq:
    def __init__(self, strbases):

        self.strbases = strbases


    def len(self):
        return len(self.strbases)

    def complement(self):
        ns = []
        for b in self.strbases:
            if b == "A":
                ns.append("T")
            elif b == "T":
                ns.append("A")
            elif b == "C":
                ns.append("G")
            elif b == "G":
                ns.append("C")
            else:
                ns.append(b)
        ns = "".join(ns)
        return ns

    def reverse(self):
        ns = []
        for i in range((-1)*(len(self.strbases)-1),1):
            ns.append(self.strbases[(-1)*i])
        ns = "".join(ns)
        return ns

    def count(self, base):
        return count_letter(self.strbases, base)

    def perc(self, base):
        return round((count_letter(self.strbases, base) * 100 / len(self.strbases)), 1)
