# Class 1
class Pakistan():
    def capital(self):
        print("Islamabad is the capital of Pakistan.")
 
    def language(self):
        print("Urdu is the most widely spoken language of Pakistan.")
 
    def type(self):
        print("Pakistan is a developing country.")
 
# Class 2
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
# Object Creation
obj_ind = Pakistan()
obj_usa = USA()

# Common Interface
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()