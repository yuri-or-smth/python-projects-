#this peece of code is made by yuri_or_smth
import math
fnum = float(input("first number: "))
snum = float(input("second number: "))
op = input("operation (+, -, *, /, ^, !): ")
if op == "+":
    print(fnum + snum)
elif op == "-":
    print(fnum - snum)
elif op == "*":
    print(fnum * snum)
elif op == "/":
    if snum != 0:
        print(fnum / snum)
    else:
        print("Error: Division by zero")
elif op == "^":
    print(fnum ** snum)
elif op == "!":
    print(math.factorial(int(fnum)))
else:
    print("Invalid operation")