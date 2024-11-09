import math

# arccos(x) returns a value in radians. rad_to_deg(radians) will convert this value to degrees
def rad_to_deg(radians):
    return radians * (180 / 3.141592653589793)

def deg_to_rad(degrees):
    return degrees * (3.141592653589793 / 180)


# The higher the term, the more accurate the result
def arccos(x, terms=10):
    if x < -1 or x > 1:
        raise ValueError("Input must be between -1 and 1 for arccos")
    if x == 1:
        return 0;
    if x == -1:
        return math.pi

    # Initialize with the first term, which is π/2 - x
    result = math.pi / 2 - x

    # Use Taylor series for accuracy
    # The higher the term, the more accurate the result
    x_pow = x  # Start with x^1
    sign = -1
    for n in range(1, terms):
        x_pow *= x * x  # Increment to the next power of x^3, x^5, etc.
        coef = (2 * n - 1) / (2 * n * (2 * n + 1))  # Coefficients: 1/6, 3/40, etc.
        result += sign * coef * x_pow
        sign *= -1  # Alternate signs

    return result

# Main
if __name__ == '__main__':
    rad = arccos(0.3)
    print(rad)
    print(rad_to_deg(rad))
    print(deg_to_rad(rad_to_deg(rad)))

