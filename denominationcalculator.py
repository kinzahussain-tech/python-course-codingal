from tkinter import *
from tkinter import messagebox

# Create window
top = Tk()
top.title("Denomination Calculator")
top.geometry("350x300")
top.configure(bg='light grey')

# Function
def calculator():
    try:
        amount = int(entry.get())

        note2000 = amount // 2000
        amount %= 2000

        note500 = amount // 500
        amount %= 500

        note100 = amount // 100

        # Clear previous values
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)

        # Insert values
        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Labels & Entry
label = Label(top, text="Enter total amount", bg='light grey')
label.pack()

entry = Entry(top)
entry.pack()

lbl = Label(top, text="Number of notes", bg='light grey')
lbl.pack()

l1 = Label(top, text="2000", bg='light grey')
l1.pack()
t1 = Entry(top)
t1.pack()

l2 = Label(top, text="500", bg='light grey')
l2.pack()
t2 = Entry(top)
t2.pack()

l3 = Label(top, text="100", bg='light grey')
l3.pack()
t3 = Entry(top)
t3.pack()

# Button
btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')
btn.pack(pady=10)

top.mainloop()