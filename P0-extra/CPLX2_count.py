from typing import List
NumA = 0
NumC = 0
NumG = 0
NumT = 0
AuxVar = open("CPLX2.txt", "r")
AuxVar: List[str] = AuxVar.splitlines()
for elem in AuxVar:
    if elem[0] != ">":
        NumA = NumA + int(elem.count('A'))
        NumC = NumC + int(elem.count('C'))
        NumG = NumG + int(elem.count('G'))
        NumT = NumT + int(elem.count('T'))
print('A:', NumA)
print('C:', NumC)
print('T:', NumT)
print('G:', NumG)