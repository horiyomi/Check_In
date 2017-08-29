import turtle


def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")
    line = turtle.Turtle()
    line.forward(100)
    line.left(90)
    line.forward(100)
    line.left(90)
    line.forward(100)
    line.left(90)
    line.forward(100)
    line.left(90)
    window.exitonclick()

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    angie = turtle.Turtle()
    angie.color("blue")
    angie.shape("turtle")
    angie.circle(100)

    window.exitonclick()

def draw_triangle():
    window = turtle.Screen()
    window.bgcolor("red")

    triangle = turtle.Turtle()
    triangle.forward(100)
    triangle.left(175)
    triangle.forward(100)
    triangle.left(270)
    triangle.forward(100)
    triangle.left(90)
    triangle.right(2)

    window.exitonclick()

# draw_shape()
# draw_circle()
draw_triangle()