import os

fName = input("What is your first name: ")
lName = input("What is your last name: ")
initialName = fName[0] + ". " + lName
 #adding strings is concatination
print("Hi, "+initialName)
os.system("say Hi"+fName+" "+lName)