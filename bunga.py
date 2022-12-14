import turtle

# Create a turtle
t = turtle.Turtle()

# Set the background color
t.screen.bgcolor("#b3daff")

# Set the turtle's speed
t.speed(10)

# Define a list of colors to use for the petals
colors = ["#ffb6c1", "#ffa07a", "#ff8c00", "#ff7f50",
          "#ffa500", "#ffdab9", "#eee8aa", "#fff0f5"]

# Define a function for drawing a petal


def draw_petal(color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(100)
        t.right(45)
        t.forward(100)
        t.right(135)
    t.end_fill()


# Move the turtle to the starting position
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw the stem
t.setheading(90)
t.forward(200)

# Draw the flower using a loop
for i in range(8):
    draw_petal(colors[i])
    t.right(45)

# Hide the turtle
t.hideturtle()
