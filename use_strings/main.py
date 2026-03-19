# name = input("Enter your full name: ")
# phone_number = input("Enter your phone #: ")
# result = len(name)
# result = name.find("Assis")
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", "")
# print(phone_number)
# print(help(str))
print("rules:\nusername is no more than 12 characters")
print("username must not contain spaces")
print("username must not contain digits")
name = input("Enter your username: ")
length = len(name)
i = 0
number= True
while i < 10:
    if name.find(str(i)) == -1:
        number = True
    else:
        number = False
        break
    i += 1

if number and name.find(" ") == -1 and length < 13 and length > 0:
    print(f"Username: {name}")
else:
    print("I don't follow the rules")
print("Bye!")