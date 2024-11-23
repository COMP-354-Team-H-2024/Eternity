
def calculate_logbx(x, b, tolerance=1e-10, max_iterations=5000):
    if x <= 0 or b <= 1:
        raise ValueError("x must be greater than 0 and base b must be greater than 1")

    low, high = 1e-5, x if x > 1 else 1
    guess = (low + high) / 2.0
    iteration = 0

    print(f"\nStarting computation for log base {b} of {x}...")
    print(f"Initial guess range: low = {low}, high = {high}\n")

    while abs(b ** guess - x) > tolerance and iteration < max_iterations:
        if b ** guess < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        if iteration % 100 == 0:
            print(f"Iteration {iteration}: guess = {guess}, error = {abs(b ** guess - x)}")
        if guess > 100:
            raise OverflowError(f"Result too large, guess exceeded max value of 100")

        iteration += 1

    if iteration == max_iterations:
        raise OverflowError("Max iterations reached, result may not be accurate")
    
    print(f"\nComputation completed in {iteration} iterations.")
    return guess

##main program
def main():
    print("This program calculates log base 'b' of a number 'x'.\n")
    while True:
        try:
       
            x = float(input("Enter the value of x (must be greater than 0): "))
            b = float(input("Enter the base b (must be greater than 1): "))
        
        
            result = calculate_logbx(x, b)
            print(f"\nlog base {b} of {x} is approximately: {result}")
    
        except ValueError as e:
            print(f"Input Error: {e}")
        except OverflowError as e:
            print(f"Computation Error: {e}")
    
    
        cont = input("\nDo you want to calculate another logarithm? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Logarithmic calculations ended!")
            break

if __name__ == "__main__":
    main()