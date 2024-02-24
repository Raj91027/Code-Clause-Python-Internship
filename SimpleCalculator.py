import tkinter as tk


def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)


def clear():
    entry.delete(0, tk.END)


def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Graphical User Interface

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input and output
entry = tk.Entry(root, width=40, borderwidth=5, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create and position buttons
for (symbol, row, col) in buttons:
    if symbol == "=":
        btn = tk.Button(root, text=symbol, padx=20, pady=20, command=calculate)
    elif symbol == "C":
        btn = tk.Button(root, text=symbol, padx=20, pady=20, command=clear)
    else:
        btn = tk.Button(root, text=symbol, padx=20, pady=20, command=lambda s=symbol: button_click(s))
    btn.grid(row=row, column=col)

root.mainloop()
