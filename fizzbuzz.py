while True:
    user_input = input("Type STOP to stop or CONT to continue")
    if user_input == "STOP":
        break
    elif user_input == "CONT":
        num1 = input("pick a number")
    else:
        digit = input("don't try to cheat the system, punk. try again. STOP to stop and CONT to continue.")
        if user_input == "STOP":
            break
        if user_input == "CONT":
            num1 = input("pick a number")
num1 = int(num1)
def fizzItUp (num1, num2):
    return num1 % num2

result = (num1 , 3)

if result == 0:
    res2 = num1 % 5
    if res2 == 0:
        print("fizzbuzz")
    if res2 != 0:
        print("fizz")
if result != 0:
    res3 = num1 % 5
    if res3 == 0:
        print ("buzz")
    if res3 != 0:
        print ("new number pls, peasant")
