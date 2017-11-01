text = "This is a Demo text"

saveFile = open('Demo.txt','w')

saveFile.write(text) # It will be in the RAM memory
saveFile.close() # This will actually save the file on the Secondary storage


readFile = open('Demo.txt','r')
print(readFile.read())
readFile.close()

appendToFile = open('Demo.txt','a')
appendToFile.write(". This is demo again.")
appendToFile.close()

appendedToFile = open('Demo.txt','r')
print(appendedToFile.read())
appendedToFile.close()