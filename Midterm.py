import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = math.pi * (radius ** 2)

    return round(area, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n < 3:
        
        return "The triangle height should be at least 4."

    result = ""
    for i in range(n):
        for j in range(n):
            if j == i or j == 0 or i == n - 1:
                result += "*"
            else:
                result += " "
        result += "\n"

    return result
print(hollow_right_triangle(5))

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    return ""

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()