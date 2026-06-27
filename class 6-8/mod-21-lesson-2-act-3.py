# Create a class
class PairElements:

    def find_pair(self, numbers, target):
        # Empty dictionary to store numbers and their indices
        data = {}

        for index, value in enumerate(numbers):
            difference = target - value

            if difference in data:
                return data[difference], index

            data[value] = index

        return None


# Main Program
numbers = (10, 20, 30, 40, 50, 60, 70)

target = int(input("Enter the target sum: "))

obj = PairElements()
result = obj.find_pair(numbers, target)

if result:
    print("Index1 =", result[0])
    print("Index2 =", result[1])
else:
    print("No pair found.")