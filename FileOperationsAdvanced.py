name = ""
namesFile = open('names.txt', 'a')

while name != "end":
    name = input("Enter the name: ")
    if name == "end":
        break
    else:
        namesFile.write(name+'\n')
namesFile.close()

readNamesFile = open('names.txt', 'r')
names = readNamesFile.readlines()
readNamesFile.close()

for n in names:
    print(n)