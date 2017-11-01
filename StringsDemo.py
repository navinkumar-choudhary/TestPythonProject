# str = ['A', 'n','k', 'p', 'r', 'o']
str = "Ankpro"
str1 = "Ankpro@)"

print(str)

msg = "python is a flexible flexi programming languge python"
print(msg[7:10]) # it will take always max range as max-1

print(msg.index('flexible'))

print(msg[msg.index('flexible'):msg.index('flexible')+12])


print(msg[:-10]) # removes last 10 chracters
print(msg[-10:]) # retrieves last 10

# below will take first 6 chars from string and concatinates with another string
print(msg[0:7]+"- I should learn")

# print the string in Initcap formatting
print(msg.capitalize())
print(msg.upper())
print(msg.lower())



msg1 = "4SM02CS106"

print(msg1.isalpha())
print(msg1.isalnum())

print(str.isalpha())
print(str.isalnum())
print(str1.isalpha())


msg = msg.replace("python","JavaScript", 1) # last Number shows the occurances to be replaced in this case only first occ will be replaced
print(msg)

strr = "  hi  "
strr = strr.strip()
print(strr)

strr = "  hi  "
print(strr.lstrip())

strr = "  hi  "

print(strr.rstrip())

