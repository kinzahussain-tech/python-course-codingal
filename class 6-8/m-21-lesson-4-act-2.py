class Computer:

    def __init__(self):
        self.__maxprice = 1000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 2000
c.sell()

# using setter function
c.setMaxPrice(500)
c.sell()