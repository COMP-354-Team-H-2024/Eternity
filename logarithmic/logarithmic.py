def Log_Base_b(x, b, tolerance=1e-10):
    if x <= 0 or b <= 1:
        raise ValueError("x must be greater than 0 and base b must be greater than 1")


    low, high = 0, x
    guess = (low + high)/2.0

    while abs(b ** guess - x) > tolerance:
        if b ** guess < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
    
    return guess


x = 10
b = 2
result = Log_Base_b(x,b)
print(f"log base {b} of {x} is approximately: {result}")
