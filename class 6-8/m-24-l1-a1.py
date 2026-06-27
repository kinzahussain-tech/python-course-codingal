
import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('Kinza', 5, 48.5), ('Mirha', 6, 52.5),('zurwa', 5, 42.10), ('height', 5, 40.11)]
# create a structured array
students = np.array(students_details, dtype=data_type)   
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))