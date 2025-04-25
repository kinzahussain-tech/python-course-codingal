def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')

# Adding a newline after each binary conversion for clarity
print("Binary of 27:", end=' ')
DecimalToBinary(27)
print()  # for making newline

print("Binary of 67:", end=' ')
DecimalToBinary(67)
print()  # for making newline

print("Binary of 114:", end=' ')
DecimalToBinary(5)
print()  # for making newline