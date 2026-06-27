import tkinter as tk

# Function to check password strength
def check_password():
    password = entry.get()
    length = len(password)

    if length < 6:
        result.config(text="Password Strength: Weak")
    elif length < 10:
        result.config(text="Password Strength: Medium")
    else:
        result.config(text="Password Strength: Strong")

# Create window
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("350x200")

# Label
tk.Label(window, text="Enter Password:").pack(pady=5)

# Password Entry
entry = tk.Entry(window, show="*")
entry.pack()

# Button
tk.Button(window, text="Check Strength", command=check_password).pack(pady=10)

# Result Label
result = tk.Label(window, text="Password Strength: ")
result.pack()

# Run the application
window.mainloop()