import turtle

def intro_example():
    print("hello") #This is only an example method for printing hello

def draw_petal():       #This func. prints a single petal (a rhombus shape), by drawing lines and angles
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

def draw_flower():    #This func. prints a flower by printing 4 petals and a stem
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

def draw_flower_and_advance(): #This func. prints a single flower (by executing the draw_flower func.), then moves the the right position to draw the next flower
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


def draw_flower_bed(): #This func. moves to the left of the screen, then draws 3 flowers by executing the draw_flower_and_advance() func. 3 times
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

if __name__ == "__main__" :     #calls functions above
    draw_flower_bed()
    turtle.done








