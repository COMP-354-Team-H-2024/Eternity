How to use each function:
1. Exponentiation (x^y):
   - Enter the base using digit buttons (0-9)
   - Use a comma "," to separate the parameter
   - Enter the exponent y using the digit buttons (0-9)
   - Press the x^y button to calculate and display the result. 
2. function a(b^x):
   - Enter the value of a using the digit buttons (0-9).
   - Use a comma "," to separate the parameters.
   - Enter the value of b using the digit buttons (0-9).
   - Use a comma "," to separate the parameters.
   - Enter the exponent x using the digit buttons (0-9).
   - Press the "a(b^x)" button to calculate and display the result.
3. Inverse Cosine arccos(x):
   - Press the "arccos(x)" button on the calculator.
   - Enter the value of x using the digit buttons (0-9).
   - Press "=" to see the result
4. Logarithm log_bx:
   - Enter the base b using the digit buttons (0-9).
   - Use a comma , to separate the base and the argument.
   - Enter the argument x using the digit buttons (0-9).
   - Press the log_bx button to calculate and display the result.
5.  Mean Absolute Deviation MAD:
   - Enter as many numbers as you want, separated by commas.
   - Press the "MAD" button to calculate and display the result.
6.  Standard Deviation (std):
   - Enter as many numbers as you want, separated by commas.
   - Press the std button to calculate and display the result.

How to run the calculator:
1. Make sure you have Python and Flask installed on your system. 
You can install Flask using pip if you do not have it:

   pip install Flask


2. Project Structure: 
calculator_project/
│
├── app.py                    # Main Flask application file
├── templates/
│   └── index.html            # HTML file for the user interface
│
├── static/
│   ├── style.css             # CSS for styling the interface
│   └── script.js             # JavaScript for handling calculator logic
│
├── abx/                # Folder for function scripts (e.g., power_function.py, arccos_function.py, etc.)
│   ├── power_function.py     # Power-related function
├── arccos_function.py    # arccos function, etc.

└── 
