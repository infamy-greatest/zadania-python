import turtle


def draw_tree(branch_length, t):

    if branch_length > 30: # Base case
        for _ in range(3):
            t.forward(branch_length)
            t.right(90)
            branch_length -= 10
        draw_tree(branch_length, t)

# Setup Turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.pensize(4)
t.color("green")
t.speed("fastest")
t.left(90) # Start pointing upwards
t.penup()
t.goto(-150, -150) # Start near the bottom of the screen
t.pendown()
# Draw fractal tree
draw_tree(300, t)
screen.exitonclick()