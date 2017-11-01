# Write a program to display user's complete mailing address.
# Accept user's name, city, street, pin num, and house num and store it in a variable and display it.

Name = input("Enter the User Name: ")
City = input("Enter your City name: ")
Street = input("Enter you street: ")
Pin = input("Enter your postal Code: ")
House_Num = input("Enter your house number: ")

print("Here is the User information")
print("Name: "+Name)
print("Address: House Number "+House_Num+", "+Street+", "+City+"-"+Pin)