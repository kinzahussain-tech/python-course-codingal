import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Update labels
    user_label.config(text="You: " + user_choice)
    comp_label.config(text="Computer: " + computer_choice)
    result_label.config(text=result)

# GUI window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x300")

# Labels
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 14))
title.pack(pady=10)

user_label = tk.Label(root, text="You: ", font=("Arial", 12))
user_label.pack()

comp_label = tk.Label(root, text="Computer: ", font=("Arial", 12))
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Buttons
btn_rock = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
btn_scissors.pack(pady=5)

# Run GUI
root.mainloop()