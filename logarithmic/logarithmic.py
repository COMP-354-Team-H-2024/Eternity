def Log_Base_b(x, b, tolerance=1e-10, max_iterations=5000):
    if x <= 0 or b <= 1:
        raise ValueError("x must be greater than 0 and base b must be greater than 1")

    low, high = 1e-5, x if x > 1 else 1
    guess = (low + high) / 2.0
    iteration = 0

    while abs(b ** guess - x) > tolerance and iteration < max_iterations:
        if b ** guess < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        if guess > 100:
            raise OverflowError(f"Result too large, guess exceeded max value of 100")

        iteration += 1

    if iteration == max_iterations:
        raise OverflowError("Max iterations reached, result may not be accurate")

    return guess


x = 10
b = 2
# result = Log_Base_b(x, b)
# print(f"log base {b} of {x} is approximately: {result}")


def calculate_logbx(x, b, tolerance=1e-10, max_iterations=5000):
    if x <= 0 or b <= 1:
        raise ValueError("x must be greater than 0 and base b must be greater than 1")

    low, high = 1e-5, x if x > 1 else 1
    guess = (low + high) / 2.0
    iteration = 0

    while abs(b ** guess - x) > tolerance and iteration < max_iterations:
        if b ** guess < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        if guess > 100:
            raise OverflowError(f"Result too large, guess exceeded max value of 100")

        iteration += 1

    if iteration == max_iterations:
        raise OverflowError("Max iterations reached, result may not be accurate")

    return guess