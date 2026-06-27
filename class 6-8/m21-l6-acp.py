# Create a class
class RomanConverter:

    # Constructor
    def __init__(self, number):
        self.number = number

    # Method to convert integer to Roman numeral
    def to_roman(self):
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        roman = ""
        num = self.number

        for value, symbol in values:
            while num >= value:
                roman += symbol
                num -= value

        return roman


# Take input from the user
num = int(input("Enter an integer: "))

# Create object
obj = RomanConverter(num)

# Display Roman numeral
print("Roman Numeral:", obj.to_roman())