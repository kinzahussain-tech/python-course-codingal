#define function to calculate cube
def cube(number):
  return number*number*number
  
#define a function which will execute cube function if the user entered number is divisible by 3
def divis_3(number):
  if number %3 ==0:
    return cube(number)
  else:
    return False
#display result
print(divis_3(9))
print(divis_3(18))