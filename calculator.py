from tkinter import *
import re

# Import functions
import power.power_function as power_function
import abx.abx as abx
import geo.arccos.arccos as arccos

def click(event):
    text = event.widget.cget("text")
    current_text = screen.get()

    if text == "=":

        # Handle power function using "^"
        if "^" in current_text:
            try:
                base, exponent = current_text.split("^")
                result = power_function.calculate_power(base, exponent)
                screen.set(result)
            except ValueError:
                screen.set("Error: Invalid input for power function.")

        # Handle arccos function
        elif "arccos(" in current_text:
            match = re.match(r"arccos\(([-+]?\d*\.\d+|\d+)\)", current_text)
            if match:
                try:
                    x = float(match.group(1))
                    result = arccos.arccos(x)
                    screen.set(result)
                except ValueError:
                    screen.set("Error: Invalid input for arccos. Must be between -1 and 1.")
            else:
                screen.set("Error: Invalid arccos format")

        elif "ab^x(" in current_text:
            match = re.match(r"ab\^x\(\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)\s*\)", current_text)
            if match:
                try:
                    a = float(match.group(1))
                    b = float(match.group(2))
                    x = float(match.group(3))
                    result = abx.calculate_abx(a, b, x)
                    screen.set(result)
                except ValueError:
                    screen.set("Error: Invalid parameters for ab^x.")
            else:
                screen.set("Error: Invalid ab^x format.")
        else:
            try:
                result = str(eval(current_text))
                screen.set(result)
            except Exception as e:
                screen.set("Error")
    elif text == "CLEAR":
        screen.set("") # Clear the screen
    elif text == "DEL":
        screen.set(current_text[:-1]) # Delete the last character
    elif text == "x^y":
        if current_text and current_text[-1].isdigit():
            screen.set(current_text + "^")
    elif "a(b^x)" in current_text:
        screen.set("a(b^x)( , , )")
    elif text == "logb(x)":
        screen.set(current_text + "log(")
    elif text == "arccos(x)":
        screen.set(current_text + "arccos(")
    elif text == "MAD":
        screen.set("MAD")
    elif text == "cos(x)":
        screen.set(current_text + "cos(")
    elif text == "sin(x)":
        screen.set(current_text + "sin(")
    else:
        # current_text = screen.get()
        screen.set(current_text + text)


root = Tk()
root.title("Calculator")

# root.config(bg="#f0f0f0")

# Screen to display input and output
screen = StringVar()

# Text display frame
frame_display = Frame(root, bd=0, relief=RAISED)  # Set border width and raised relief
frame_display.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

entry = Entry(frame_display, textvar=screen, font="lucida 15 bold", width=40, bd=2)
entry.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

# Button frame
frame_buttons = Frame(root)
frame_buttons.pack()

buttons = [
    'x^y', 'a(b^x)', 'log_b(x)', 'arccos(x)','MAD',
    'σ', 'e', 'π', '(', ')',
    '7', '8', '9', 'DEL', 'CLEAR',
    '4', '5', '6', '+', '*',
    '1', '2', '3', '-','/',
    '0', '.', '%', ',','='
]

row = 0
col = 0

button_fg = 'darkgreen'

for button in buttons:
    btn = Button(frame_buttons, text=button, font="lucida 20 bold", padx=15, pady=20, width=3, height=1,
                 fg=button_fg)
    btn.grid(row=row, column=col, padx=3, pady=2)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()