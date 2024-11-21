def calculate_sine(x, terms=10):
    sine_value = 0
    for n in range(terms):
        # Calculate (-1)^n
        sign = (-1) ** n
        # Calculate (2n + 1)!
        factorial = 1
        for i in range(1, 2*n + 2):
            factorial *= i
        # Calculate x^(2n + 1)
        power = x ** (2 * n + 1)
        # Add term to sine value
        sine_value += sign * (power / factorial)
    return sine_value

# Example usage:
x_value = 180.0  # Replace with any value (in radians)
result = calculate_sine(x_value)
print(f"The sine of {x_value} (using Taylor series approximation) is {result}")
