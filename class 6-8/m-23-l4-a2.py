import tkinter as tk

# Function to calculate SI and CI
def calculate():
    principal = float(entry_principal.get())
    rate = float(entry_rate.get())
    time = float(entry_time.get())

    # Simple Interest
    si = (principal * rate * time) / 100

    # Compound Interest
    amount = principal * (1 + rate / 100) ** time
    ci = amount - principal

    result_si.config(text="Simple Interest = {:.2f}".format(si))
    result_ci.config(text="Compound Interest = {:.2f}".format(ci))


# Create window
window = tk.Tk()
window.title("Interest Calculator")
window.geometry("400x300")

# Labels and Entry Boxes
tk.Label(window, text="Principal Amount:").pack()
entry_principal = tk.Entry(window)
entry_principal.pack()

tk.Label(window, text="Rate of Interest (%):").pack()
entry_rate = tk.Entry(window)
entry_rate.pack()

tk.Label(window, text="Time (Years):").pack()
entry_time = tk.Entry(window)
entry_time.pack()

# Button
tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

# Result Labels
result_si = tk.Label(window, text="Simple Interest = ")
result_si.pack()

result_ci = tk.Label(window, text="Compound Interest = ")
result_ci.pack()

# Run application
window.mainloop()