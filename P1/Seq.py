def count_letter(arg1, arg2):
    n_characters = 0   # Counter for the characters
    for b in arg1:
        if b == arg2:
            n_characters += 1
    return n_characters

class Seq:
    def __init__(self, strbases):

        self.strbases = strbases
        aux_list = []
        for line in strbases:
            aux_list.append(line)
        aux_list = aux_list[1:]
        ns = " ".join(aux_list)
        self.strbases = ns


    def len(self):
        return len(self.strbases)

    def complement(self):
        ns = str()
        for b in self.strbases:
            if b == "A":
                ns.join("T")
            elif b == "T":
                ns.join("A")
            elif b == "C":
                ns.join("G")
            elif b == "G":
                ns.join("C")
        return ns

    def reverse(self):
        ns = str()
        for i in range((-1)*len(self.strbases),0):
            ns.join(str((-1)*i))
        return ns

    def count(self, base):
        return count_letter(self.strbases, base)

    def perc(self, base):
        return count_letter(self.strbases, base) * 100 / len(self.strbases)
