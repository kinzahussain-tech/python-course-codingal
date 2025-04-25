def add(X, Y):    
   # This function is used for adding two numbers   
   return X + Y   
def subtract(X, Y):   
   # This function is used for subtracting two numbers  
   return X - Y   
def multiply(X, Y):   
   # This function is used for multiplying two numbers  
   return X * Y   
def divide(X, Y):   
   # This function is used for dividing two numbers    
   return X / Y 
      
# Now we will take inputs from the user    
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
option = input("Please enter choice (a/ b/ c/ d): ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if option == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif option == 'b':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif option == 'c':    
   print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))  

elif option == 'd':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))    
else:    
   print ("This is an invalid input")    