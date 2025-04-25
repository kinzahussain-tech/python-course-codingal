def squareperimeter(x):
  perimeter=4*x
  print("perimeter of square is",perimeter)

def rectangleperimeter(length,breadth):
  perimeter = 2*(length+breadth)
  return perimeter

def circumference(r):
  circum=2*3.14*r
  print("circumference of circle is",circum)

radius=int(input("enter radius of circle:"))
circumference(radius)

x=int(input("Enter side of square->"))
squareperimeter(x)

length = int(input("Enter length of rectangle->"))
breadth = int(input("Enter breadth of rectangle->"))
print(rectangleperimeter(length,breadth))