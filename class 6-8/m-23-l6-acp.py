import tkinter as tk
import random

# Function to play the game
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    computer_label.config(text="Computer: " + computer_choice)
    result_label.config(text="Result: " + result)

# Create window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("350x250")

# Heading
tk.Label(window, text="Choose Rock, Paper or Scissors", font=("Arial", 12)).pack(pady=10)

# Buttons
tk.Button(window, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
tk.Button(window, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
tk.Button(window, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=5)

# Labels for output
computer_label = tk.Label(window, text="Computer: ")
computer_label.pack(pady=5)

result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=5)

# Run the application
window.mainloop()