from tkinter import *
import re

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "CLEAR":
        screen.set("")
    elif text == "ab^x":
        screen.set("Enter a*b^x:")
    else:
        current_text = screen.get()
        if current_text.startswith("Enter a*b^x:"):
            screen.set(current_text + text)
        else:
            screen.set(current_text + text)


root = Tk()
root.title("Calculator")

screen = StringVar()
entry = Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

frame = Frame(root)
frame.pack()

buttons = [
    'ab^x', 'xy', 'arcos(x)', 'MAD',
    'logb(x)', 'σ', '(', ')',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'CLEAR', '0', '=', '+'
]

row = 0
col = 0
for button in buttons:
    btn = Button(frame, text=button, font="lucida 15 bold", padx=20, pady=20)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1   

root.mainloop()