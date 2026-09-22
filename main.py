"""Task 1: Calculate the area of a circle."""

from math import pi

radius = float(input("Enter the radius of the circle: "))

if radius < 0:
    print("The radius cannot be negative.")
else:
    area = pi * radius ** 2
    print(f"The area of the circle is: {area:.2f}")
