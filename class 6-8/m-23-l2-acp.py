import tkinter as tk
from datetime import date

# Function to calculate age
def calculate_age():
    day = int(entry_day.get())
    month = int(entry_month.get())
    year = int(entry_year.get())

    today = date.today()

    age = today.year - year

    # Check if birthday has occurred this year
    if (today.month, today.day) < (month, day):
        age -= 1

    result.config(text="Present Age = " + str(age) + " years")


# Create window
window = tk.Tk()
window.title("Age Calculator")
window.geometry("350x250")

# Labels and Entry Boxes
tk.Label(window, text="Enter Birth Day:").pack()
entry_day = tk.Entry(window)
entry_day.pack()

tk.Label(window, text="Enter Birth Month:").pack()
entry_month = tk.Entry(window)
entry_month.pack()

tk.Label(window, text="Enter Birth Year:").pack()
entry_year = tk.Entry(window)
entry_year.pack()

# Button
tk.Button(window, text="Calculate Age", command=calculate_age).pack(pady=10)

# Result Label
result = tk.Label(window, text="Present Age = ")
result.pack()

# Run application
window.mainloop()
