import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("435x635")
window.configure(bg="#202531")
window.iconbitmap(r"D:\python calculator\calc.ico")
window.resizable(False, False)


# === Display ===
display = tk.Entry(
    window,
    font=("Segoe UI", 32),
    bg="#202531",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="black",
    relief="flat",
    width=17
)
display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=20,
    pady=30,
    ipady=25
)

# === buttons ===
buttons = [
    ["CE", "C", "⌫", "+"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "/"],
    ["+/-", "0", ".", "="]
]

# === button functions ===
def on_click(value):
    if value == "C":
        display.delete(0, tk.END)
    elif value == "⌫":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current[:-1])
    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif value == "+/-":
        current = display.get()
        if current.startswith("-"):
            display.delete(0, tk.END)
            display.insert(0, current[1:])
        elif current:
            display.delete(0, tk.END)
            display.insert(0, "-" + current)
    elif value == "CE":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)

# === Generate button ===
for row_index, row in enumerate(buttons):
    for col_index, button_text in enumerate(row):
        button = tk.Button(
            window,
            text=button_text,
            font=("Segoe UI", 18),
            width=5,
            height=2,
            bd=0,
            bg="#2e2e2e",
            fg="white",
            activebackground="#4e4e4e",
            command=lambda val=button_text: on_click(val)
        )
        button.grid(row=row_index+1, column=col_index, padx=5, pady=5, sticky="nsew")

# === run program ===
window.mainloop()