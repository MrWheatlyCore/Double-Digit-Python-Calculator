print("Double Digit Calculator")
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
equation = input("Equation (+, -, *, /)")
if equation == "+":
    print(num1 + num2)
elif equation == "-":
    print(num1 - num2)
elif equation == "*":
    print(num1 * num2)
elif equation == "/":
    print(num1 / num)
else:
    print("SYNTAX ERROR")