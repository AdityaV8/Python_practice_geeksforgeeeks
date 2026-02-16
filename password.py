password = input("Enter new password : ")
result = []

#checks for length
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

#check for digit
digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

#check for uppercase letter
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result.append(uppercase)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")



















# string = "........."
# print(string.replace(".","-",2))
