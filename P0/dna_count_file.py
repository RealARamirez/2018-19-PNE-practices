SelectedFile = input("Write the name of the file: ")
with open(SelectedFile, "r") as f:
    f.strip('\n')
    print('Total length:', len(f))
    print('A:', f.count('A'))
    print('C:', f.count('C'))
    print('T:', f.count('T'))
    print('G:', f.count('G'))
