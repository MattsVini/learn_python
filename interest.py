name = input("What's your name? ")
balance_base = float(input("how many you would like give safe money on the bank? "))
tax = float(input("What is a quantity of borrowing percent per year? "))
interest = balance_base * (tax/100)
flag = True
def increase_amount(increasing):
    return increasing + balance_base

while flag:
    flagtwo = True
    interest = balance_base * (tax / 100)
    print()
    print("Ok:")
    print(f"Name: {name}")
    print(f"Balance: ${balance_base:.2f}")
    print(f"Interest of {tax:.2f} per year: {interest:.2f}")

    result = input("Do you would like to leave? (s/n)")
    if result.lower() == "s":
        flag = False
        break
    else:
        while flagtwo:
            change = input("What you do would like to change? interest(i), approach(a) or exit(e): ")
            if change.lower() == "i":
                tax = float(input("Type value of interest: "))

            elif change.lower() == "a":
                value = float(input("Type value for approach"))
                balance_base = increase_amount(value)
            elif change.lower() == "e":
                print("Backing...")
                flagtwo = False
            else:
                print("input ERROR!\n")
