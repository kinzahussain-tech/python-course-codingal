import math
#using ceil and floor function of math module
print('The Floor and Ceiling value of 13.26 are: ' + str(math.ceil(13.26)) + ', ' + str(math.floor(213.26)))

x = 13
y = -9
#using copysign function
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))

#using fabs and gcd function
print('Absolute value of -16 and 52 are: ' + str(math.fabs(-16)) + ', ' + str(math.fabs(52)))

print('The GCD of 72 and 66 : ' + str(math.gcd(72, 66)))