def quadratic_equation(a,b,c):   # this function takes the coefficients a,b,c of a*x^2 +b*x + c and solve the quadratic equation
    a = float(a)    #converts nums a,b,c into floats
    b = float(b)
    c = float(c)
    x = (-b + (b**2 - 4*a*c)**0.5)/(2*a) # evaluates the positive discriminant solution
    y = (-b - (b**2 - 4*a*c)**0.5)/(2*a) # evaluates the negative discriminant solution

    if (b**2 - 4*a*c) > 0:   # check cases for a single solution and no solution and return None for no solution
        return x, y
    elif (b**2 - 4*a*c) == 0:
        return x, None
    else:
        return None, None

def quadratic_equation_user_input():        # inputs coeffiecients a,b,c from the user and split it to 3
    coefficients = input('Insert coefficients a, b, and c:').split()
    a = float(coefficients[0])    #converts nums a,b,c into floats
    if (a == 0 or len(coefficients) == 2):          # check case for a = 0, and if a = 0 it asks users to chose a different value
        print("The parameter 'a' may not equal 0")
        return None
    b = float(coefficients[1])
    c = float(coefficients[2])

    x = (-b + (b**2 - 4*a*c)**0.5)/(2*a) # evaluates the positive discriminant solution
    y = (-b - (b**2 - 4*a*c)**0.5)/(2*a) # evaluates the negative discriminant solution

    if (b**2 - 4*a*c) > 0: # check cases for a single solution and no solution and return None for no solution
        print(f'The equation has 2 solutions: {x} and {y}')  # this part print out how many solutions we have and what are they
        return x, y
    elif (b**2 - 4*a*c) == 0:
        print(f'The equation has 1 solution: {x}')
        return x, None
    else:
        print(f'The equation has no solutions')
        return None, None

