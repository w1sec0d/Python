firstName = str(input("Enter your first name: "))
lastName = str(input("Enter your last name: "))
reversedFirstName = str()
reversedLastName = str()
for x in range(len(firstName)-1, -1, -1):
    reversedFirstName += firstName[x]+" "
for x in range(len(lastName)-1, -1, -1):
    reversedLastName += lastName[x]+" "
print("Hello", lastName, firstName)
print("Your reversed name:", reversedFirstName)
print("Your reversed last name:", reversedLastName)
