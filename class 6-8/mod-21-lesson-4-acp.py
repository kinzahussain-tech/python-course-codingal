# Create a class
class ReverseString:

    # Constructor
    def __init__(self, text):
        self.text = text

    # Method to reverse words
    def reverse_words(self):
        words = self.text.split()
        reversed_text = " ".join(words[::-1])
        return reversed_text


# Take input from the user
sentence = input("Enter a string: ")

# Create object
obj = ReverseString(sentence)

# Display reversed string
print("Reversed String:", obj.reverse_words())