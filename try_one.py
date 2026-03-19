print("Hello guys!")
flag = True
compatibility = 1
vector  = []
def switch():
    return input("Do wish type you would like?: String(S) Float(F) Integer(I)")


def show_trigger():
    print(f"Okay, type chose {key_word}")

def end():
    print("Bye!")

while flag:
    key_word = switch().upper()
    show_trigger()
    if key_word == "S" or key_word == "F" or key_word == "I":
        count = 0
        flagtwo = 1
        while flagtwo == 1:
            if key_word == "S":
                while flagtwo == 1:
                    value = input("Type a string: ")
                    vector.append(value)
                    print(vector)
                    flagtwo = int(input("Do Wish continue with Strings? 1 == yes or other number to leave: \n"))
            elif key_word == "F":
                while   flagtwo == 1:
                    value = input("Type a float ")
                    vector.append(float(value))
                    print(vector)
                    count += 1
                    flagtwo = int(input("Do Wish continue with float? 1 == yes or other number to leave: \n"))
            else:
                while   flagtwo == 1:
                    value = input("Type an integer: ")
                    vector.append(int(value))
                    print(vector)
                    count += 1
                    flagtwo = int(input("Do Wish continue with integer? 1 == yes or other number to leave: \n"))

    else:
        process = input("Do you would like to continue? (y/n)")
        if not process == "y".lower():
            break
        else:
            print("Returning...")
            print("Calm down! Trying :-)")

end()