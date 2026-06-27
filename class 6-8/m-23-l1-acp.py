import tkinter as tk

# Function to calculate product
def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    result.config(text="Product = " + str(product))

# Create window
window = tk.Tk()
window.title("Product Calculator")
window.geometry("300x200")

# Labels and Entry boxes
tk.Label(window, text="Enter First Number:").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter Second Number:").pack()
entry2 = tk.Entry(window)
entry2.pack()

# Button
tk.Button(window, text="Calculate Product", command=multiply).pack(pady=10)

# Result Label
result = tk.Label(window, text="Product = ")
result.pack()

# Run application
window.mainloop()