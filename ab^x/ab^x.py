import re

def abx():
    userInput = input("Enter the function in form of a*b^x: ")
    match = re.match(r"([\d.]+)\s*\*\s*([\d.]+)\s*\^\s*([\d.-]+)", userInput)
    if match:
        a = float(match.group(1))
        b = float(match.group(2))
        x = float(match.group(3))
        if b == 1:
            print("The growth/decay factor (b) must not equal 1")
        else:
            y = a * (b ** x)
            print(y)
    else:
        print("Not in form of a*b^x")
abx()