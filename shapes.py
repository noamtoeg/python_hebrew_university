import math

def shape_area():

    def area_of_a_circle():     # this func. inputs the value for the radius, then calculates and returns the area of the circle
        radius = float(input())
        return math.pi * radius**2

    def area_of_a_rectangle():  # this func. inputs the value for the 2 sides of a rectange,
        a = float(input())      # then calculates and returns the area of the rectangle
        b = float(input())
        return a * b

    def area_of_an_equilateral_triangle(): # this func. inputs the value for the side of a an equilateral triangle,
        a = float(input())                 # then calculates and returns the area of the triangle
        return 0.25*math.sqrt(3)*(a**2)

    shape = int(input('Choose shape (1=circle, 2=rectangle, 3=triangle): '))     # let user chose a shape by inputing a number
    if (shape != 1) and (shape != 2) and (shape != 3): # in case user chose different than 1,2,3, the fun. will return None
        return None
    elif shape == 1:        # this condition looks at the choice of the user and execute the right area function
        area_of_a_circle()
    elif shape == 2:
        area_of_a_rectangle()
    elif shape == 3:
        area_of_an_equilateral_triangle()

