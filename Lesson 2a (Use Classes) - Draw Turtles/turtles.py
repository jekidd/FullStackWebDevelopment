import turtle

#Initialize and customize window
window = turtle.Screen()
window.bgcolor("black")

def draw_square(some_turtle):
    for x in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_circle():
    #Initialize and customize turtle "angie"
    angie = turtle.Turtle()
    angie.shape('turtle')
    angie.color('yellow')

    #Draw
    angie.circle(100)
def draw_triangle():
    #Initialize and customize turtle "todd"
    todd = turtle.Turtle()
    todd.shape('turtle')
    todd.color('green')

    #Draw
    todd.left(90)
    todd.forward(120)
    todd.left(143.1)
    todd.forward(150)
    todd.left(126.9)
    todd.forward(90)

def draw_shapes():
    #Initialize and customize turtle "brad"
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('orange')
    brad.speed(2)

    #Draw
    draw_square(brad)
    draw_circle()
    draw_triangle()

    #Pause
    window.exitonclick()

def draw_circle_with_squares():
    #Initialize and customize turtle "brad"
    frank = turtle.Turtle()
    frank.shape('turtle')
    frank.color('purple')
    frank.speed(15)

    numberOfSquares = 60
    turnAngle = 360 / numberOfSquares

    #Draw
    for x in range(0, numberOfSquares):
        draw_square(frank)
        frank.right(turnAngle)

draw_circle_with_squares()
draw_shapes()
