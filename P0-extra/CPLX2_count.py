NumA = 0
NumC = 0
NumG = 0
NumT = 0
File = open("CPLX2.txt", "r")
AuxVarRead = File.read()
AuxVar = AuxVarRead.split("\n")
for elem in AuxVar:
    try:
        if elem[0] != ">":
            NumA = NumA + int(elem.count('A'))
            NumC = NumC + int(elem.count('C'))
            NumG = NumG + int(elem.count('G'))
            NumT = NumT + int(elem.count('T'))
    except IndexError:
        continue
print('A:', NumA)
print('C:', NumC)
print('T:', NumT)
print('G:', NumG)
File.close()