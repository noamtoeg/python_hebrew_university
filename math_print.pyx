import math  #imports maths module

def golden_ratio(): # this func. generates the golden ratio phi
    print((math.sqrt(5)+1)/2)

def six_squared():  #this func. calculate 6 squared
    print(6**2)

def hypotenuse(): # this func. solves for the hypotenuse of a Pythagorean triangle of sides of 5 and 12
    print(math.sqrt(5**2 + 12**2))

def pi(): # this func. returns Pi
    print(math.pi)

def e():    # this func. returns e (exponential)
    print(math.exp(1))

def squares_area(): # this func. returns all the squared whole numbers between 1 and 10
    print(1*1,2*2,3*3,4*4,5*5,6*6,7*7,8*8,9*9,10*10)
    
if __name__ == "__main__" : #calls functions above
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
