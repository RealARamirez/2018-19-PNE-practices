from Seq import Seq
# Create sequences objects from inputs
Seq1 = input("Type the mother sequence on sequences one, three and four: ")
Seq2 = input("Type the sequence two: ")
Sequence_one = Seq(Seq1)
Sequence_two = Seq(Seq2)
Sequence_three = Seq(Sequence_one.complement())
Sequence_four = Seq(Sequence_three.reverse())
# Main program
print("Sequence 1: {}".format(Sequence_one.strbases))
print("\tLength: {}".format(Sequence_one.len()))
print("\tBases count: A:{}, T:{}, C:{}, G:{}".format(Sequence_one.count("A"), Sequence_one.count("T"), Sequence_one.count("C"), Sequence_one.count("G")))
print("\tBases percentage: A:{}%, T:{}%, C:{}%, G:{}%".format(Sequence_one.perc("A"), Sequence_one.perc("T"), Sequence_one.perc("C"),Sequence_one.perc("G")))
print("\n\nSequence 2: {}".format(Sequence_two.strbases))
print("\tLength: {}".format(Sequence_two.len()))
print("\tBases count: A:{}, T:{}, C:{}, G:{}".format(Sequence_two.count("A"), Sequence_two.count("T"), Sequence_two.count("C"), Sequence_two.count("G")))
print("\tBases percentage: A:{}%, T:{}%, C:{}%, G:{}%".format(Sequence_two.perc("A"), Sequence_two.perc("T"), Sequence_two.perc("C"), Sequence_two.perc("G")))
print("\n\nSequence 3: {}".format(Sequence_three.strbases))
print("\tLength: {}".format(Sequence_three.len()))
print("\tBases count: A:{}, T:{}, C:{}, G:{}".format(Sequence_three.count("A"), Sequence_three.count("T"), Sequence_three.count("C"), Sequence_three.count("G")))
print("\tBases percentage: A:{}%, T:{}%, C:{}%, G:{}%".format(Sequence_three.perc("A"), Sequence_three.perc("T"), Sequence_three.perc("C"), Sequence_three.perc("G")))
print("\n\nSequence 4: {}".format(Sequence_four.strbases))
print("\tLength: {}".format(Sequence_four.len()))
print("\tBases count: A:{}, T:{}, C:{}, G:{}".format(Sequence_four.count("A"), Sequence_four.count("T"), Sequence_four.count("C"), Sequence_four.count("G")))
print("\tBases percentage: A:{}%, T:{}%, C:{}%, G:{}%".format(Sequence_four.perc("A"), Sequence_four.perc("T"), Sequence_four.perc("C"), Sequence_four.perc("G")))

