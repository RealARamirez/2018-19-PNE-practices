from Seq import Seq

# Create a function that allow us to solve what our server is expected to do
# First argument must be an object of type Seq that is given by the user
# Second argument is the command that are given by the user and describe the different operations
def command_proccessor(seq, comm):
    seq = Seq(seq)
    if comm == "len":
        return seq.len()
    elif comm == "complement":
        return seq.complement()
    elif comm == "reverse":
        return seq.complement()
    elif comm == "countA":
        return seq.count("A")
    elif comm == "countT":
        return seq.count("T")
    elif comm == "countG":
        return seq.count("G")
    elif comm == "countC":
        return seq.count("C")
    elif comm == "percA":
        return seq.perc("A")
    elif comm == "percT":
        return seq.perc("T")
    elif comm == "percG":
        return seq.perc("G")
    elif comm == "percC":
        return seq.perc("C")
    else:
        return "Operation not recognised"



