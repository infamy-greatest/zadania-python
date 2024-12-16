import turtle
def draw_tree(branch_length, t):
    if branch_length > 5: # Base case
        # Draw main branch
        t.forward(branch_length)
        # Recursive call for the right subtree
        t.right(20)
        draw_tree(branch_length - 15, t)
        # Return to the main branch and adjust direction
        t.left(40)
        draw_tree(branch_length - 15, t)
        # Reset orientation
        t.right(20)
        t.backward(branch_length)
# Setup Turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.color("green")
t.speed("fastest")
t.left(90) # Start pointing upwards
t.penup()
t.goto(0, -300) # Start near the bottom of the screen
t.pendown()
# Draw fractal tree
draw_tree(100, t)
screen.exitonclick()
