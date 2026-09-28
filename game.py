import turtle as tl

screen = tl.Screen()

screen.setup(width=800, height=600)
screen.title("Pong")

player = tl.Turtle()
player.penup()
player.goto(x=-350, y=0)
player.shape("square")
player.shapesize(5,1)

opponent = tl.Turtle()
opponent.penup()
opponent.goto(x=350, y=0)
opponent.shape("square")
opponent.shapesize(5,1)

ball = tl.Turtle()
ball.penup()
ball.shape("circle")

def move_up():
    current_x = player.xcor()
    current_y = player.ycor()
    if current_y < 250:
        player.goto(current_x, current_y + 10)
    else:
        player.goto(current_x, current_y)
    
def move_down():
    current_x = player.xcor()
    current_y = player.ycor()
    if current_y > -250:
        player.goto(current_x, current_y - 10)
    else:
        player.goto(current_x, current_y )

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.listen()

tl.done()