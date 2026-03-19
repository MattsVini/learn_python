number = int(input("Enter a # between 1 - 10: "))

while number < 1 or number > 10:
    print(f"{number} is not valid")
    number = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {number}")
