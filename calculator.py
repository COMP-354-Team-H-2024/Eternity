from tkinter import *
import re
import tkinter as tk
# Import functions
from power_function import calculate_power
from abx.abx import calculate_abx
from geo.arccos.arccos import arccos

def click(event):
    text = event.widget.cget("text")
    current_text = screen.get()

    if text == "=":
        if "^" in current_text:
            base, exponent = current_text.split("^")
            result = calculate_power(base, exponent)
            screen.set(result)

        elif "ab^x" in current_text:
            match = re.match(r"([\d.]+)\s*\*\s*([\d.]+)\s*\^\s*([\d.-]+)", current_text)
            if match:
                a = float(match.group(1))
                b = float(match.group(2))
                x = float(match.group(3))
                result = calculate_abx(a, b, x)
                screen.set(result)
            else:
                screen.set("Error: Invalid ab^x format")

        elif "arccos(" in current_text:
            match = re.match(r"arccos\(([-+]?\d*\.\d+|\d+)\)", current_text)
            if match:
                x = float(match.group(1))
                try:
                    result = arccos(x)
                    screen.set(result)
                except ValueError:
                    screen.set("Error: Invalid input for arccos. Must be between -1 and 1.")
            else:
                screen.set("Error: Invalid arccos format")

        else:
            try:
                result = str(eval(current_text))
                screen.set(result)
            except Exception as e:
                screen.set("Error")
    elif text == "CLEAR":
        screen.set("") # Clear the screen
    elif text == "DEL":
        screen.set(current_text[:1]) # Delete the last character
    elif text == "x^y":
        if current_text and current_text[-1].isdigit():
            screen.set(current_text + "^")
    elif text == "ab^x":
        if current_text and current_text[-1].isdigit():
            screen.set(current_text + "^")
    elif text == "logb(x)":
        if current_text and current_text[-1].isdigit():
            screen.set(current_text + "log")
    elif text == "arccos(x)":
        screen.set("arccos(")
        if current_text and current_text[-1].isdigit():
            screen.set(current_text + "arccos")
    elif text == "MAD":
        if current_text and current_text[-1].isdigit():
            screen.set(current_text + "^")
    elif text == "cos(x)":
        screen.set("cos(")
        if current_text and current_text[-1].isdigit():
            screen.set(current_text + "cos")
    elif text == "sin(x)":
        screen.set("sin(")
        if current_text and current_text[-1].isdigit():
            screen.set(current_text + "sin")
    else:
        # current_text = screen.get()
        if current_text.startswith("Enter a*b^x:"):
            screen.set(current_text + text)
        else:
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
    'x^y', 'ab^x', 'logb(x)', 'arccos(x)','MAD',
    'σ', 'sin(x)', 'cos(x)', '(', ')',
    '7', '8', '9', 'DEL', 'CLEAR',
    '4', '5', '6', '+', '*',
    '1', '2', '3', '-','/',
    '0', '.', '%', '=','op'
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