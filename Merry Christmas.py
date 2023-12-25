import turtle, random
screen=turtle.Screen()
#title of the screen
screen.title("Merry Christmas")
#backgroundcolor of screen
screen.bgcolor("Midnight Blue")

def draw_tree():
    # Creating Right half of the tree
    turtle.color("green")
    turtle.pensize(5)
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(150)
    turtle.forward(90)
    turtle.right(150)
    turtle.forward(60)
    turtle.left(150)
    turtle.forward(60)
    turtle.right(150)
    turtle.forward(40)
    turtle.left(150)
    turtle.forward(100)
    turtle.end_fill()

    #left half of the tree
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(100)
    turtle.left(150)
    turtle.forward(40)
    turtle.right(150)
    turtle.forward(60)
    turtle.left(150)
    turtle.forward(60)
    turtle.right(150)
    turtle.forward(90)
    turtle.left(150)
    turtle.forward(133)
    turtle.end_fill()

    #Creating the trunck of the tree
    turtle.color("brown")
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(80)
    turtle.end_fill()

#Creating the balls on the Christmas Tree
def draw_balls():
    ball_coordinates = [(110, -10), (-120, -10), (100, 40), (-105, 38), (85, 70), (-95, 70)]
    for i in range(len(ball_coordinates)):
        x, y = ball_coordinates[i]
        ball_size = random.randint(7, 10)
        colr = random.choice(["red", "yellow", "white"])
        turtle.penup()
        turtle.color(colr)
        turtle.goto(x, y)
        turtle.begin_fill()
        turtle.circle(ball_size)
        turtle.end_fill()

#Drawing the bells using turtle.
def draw_bells():
    turtle.shape("triangle")
    turtle.fillcolor("yellow")
    turtle.goto(-20,30)
    turtle.setheading(90)
    turtle.stamp()
    turtle.fillcolor("red")
    turtle.goto(20,60)
    turtle.setheading(90)
    turtle.stamp()
    turtle.goto(-40,75)
    turtle.setheading(90)
    turtle.stamp()

# Printing the star using for loop
def star():
    turtle.speed(1)
    turtle.penup()
    turtle.color("yellow")
    turtle.goto(-20,110)
    turtle.begin_fill()
    turtle.pendown()

    for i in range(5):
        turtle.forward(40)
        turtle.right(144)

    turtle.end_fill()


def draw_star(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_stars_in_sky():
    turtle.speed(0)
    turtle.hideturtle()
    for _ in range(50):
        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
        size = random.randint(5, 20)
        color = random.choice(["white", "yellow", "gold"])
        turtle.penup()
        turtle.setpos(x, y)
        turtle.pendown()
        draw_star(size, color)
        
draw_tree()
draw_balls()
draw_bells()
star()

# Display the message on the screen
turtle.penup()
message="Merry Christmas!!!"
turtle.goto(-10,-180)
turtle.color("Orange")
turtle.pendown()
turtle.write(message,move=False,align="center",font=("Arial",25,"bold"))
turtle.goto(-10,-200)
turtle.color('white')
turtle.write('by - @tech.programmer.70',move=False,align="center",font=("Arial",10,"bold"))
draw_stars_in_sky()
turtle.hideturtle()
turtle.done()