import math

numberOne = input("Enter the latitude and longitude of first point on earth surface: ")
numberTwo = input("Enter the latitude and longitude of second point on earth surface: ")

x1, y1 = numberOne.split(',')
x2, y2 = numberTwo.split(',')

x1 = math.radians(float(x1))
y1 = math.radians(float(y1))
x2 = math.radians(float(x2))
y2 = math.radians(float(y2))

radius_of_the_earth = 6371.01 

distance_between_two_points = radius_of_the_earth * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print(distance_between_two_points)
