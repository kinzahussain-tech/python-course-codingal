# Define a function called hotel_cost with one argument nights as input.
def hotel_cost(nights):
    return 140*nights

#Define a function called plane_ride_cost that takes a string, city, as input.
def plane_ride_cost(city):
    if "newyork" == city:
        return 183
    elif "Austin" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "San Francisco" == city:
        return 475

#Define a function called rental_car_cost with an argument called days    
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days
        
#Define a function called trip cost with argument day, money and city
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
	
print("Cost of car rental: ",rental_car_cost(5))

print("Cost of plane ride: ",plane_ride_cost("San Francisco"))

print("Cost of hotel room: ", hotel_cost(7))

print("Total cost of the trip:",trip_cost("San Francisco",7,500))

print(trip_cost("Austin",6,500))