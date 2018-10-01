

print("********")


for i in range(4,12,2):
	print(i)

print("****BACKWARDS****")

for i in range(10,-1,-1):
	print(i)

print("***Printing String Characters***")
str = "Monkey"
for i in range(0, len(str), 1):
	print(str[i])

print("MOVING ON")
print("****PRINT STRING IN REVERSE****")
for i in range (len(str)-1,-1,-1):
	print(str[i])

print("***PRINT EVERY SECOND LETTER IN STR START AT INDEX 0***")
for i in range (0,len(str),2):
	print(str[i])

