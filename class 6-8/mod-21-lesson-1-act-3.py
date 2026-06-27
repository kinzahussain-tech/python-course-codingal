# create class
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
phoenix = Parrot("phoenix", 10)
dorik = Parrot("dorik", 15)

# access the class attributes
print("phoenix is a {}".format(phoenix.species))
print("dorik is also a {}".format(dorik.species))

# access the instance attributes
print("{} is {} years old".format( phoenix.name, phoenix.age))
print("{} is {} years old".format( dorik.name, dorik.age))