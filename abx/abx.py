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


def calculate_abx(a, b, x):
    if b == 1:
        return "The growth/decay factor (b) must not equal 1"
    else:
        y = a * (b ** x)
        return y


def main():
    a = float(input("Enter the value for a: "))
    b = float(input("Enter the value for b: "))
    x = float(input("Enter the value for x: "))

    result = calculate_abx(a, b, x)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
