# This is a ping pong game

# using turtle module

import turtle
import winsound
import random

wind = turtle.Screen()
wind.title("Ping_Pong by David Ebube")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)


# Score
score_a = 0
score_b = 0


# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)



# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Ball movement
ball.dx = 0.3
ball.dy = -0.3


# random colour change
def random_color_change():
	r = random.random()
	g = random.random()
	b = random.random()

	paddle_a.color(r, g, b)
	paddle_b.color(b, r, g)
	ball.color(r, b, b)
	wind.bgcolor(r, r, b)

def


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 15, "normal" ))

# Movement of paddles
# Functions

def paddle_a_up():
	y =  paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y =  paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)



# up movement Key binding
wind.listen()
# listens for keyboard input
wind.onkeypress(paddle_a_up, "w")
wind.onkeypress(paddle_a_down, "s")

wind.onkeypress(paddle_b_up, "Up")
wind.onkeypress(paddle_b_down, "Down")




# Borders

# Main game loop
while True:
	wind.update()

	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound("Ball_Bounce.wav", winsound.SND_ASYNC)

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound("Ball_Bounce.wav", winsound.SND_ASYNC)

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal" ))

	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal" ))

	# Paddle and ball collisions
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ):
		ball.setx(-340)
		ball.dx *= -1

	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
		ball.setx(340)
		ball.dx *= -1


	if (score_a is 5 and score_a > score_b and score_a != score_b ) :

		# temp1 = paddle_a
		# paddle_a = paddle_b
		# paddle_b = temp1

		random_color_change()
		

	# score = 5 *
	# for




	# Background and Ball color change

	# def winner():
	# 	if score_a == 10:
	# 		pen.write("PLAYER A WINS")
	# 	elif score_b == 10:
	# 		pen.write("PLAYER B WINS")
	# 		return

	# if (score_a == 10):
	# 	wind.clear()
	# 	pen.goto(0,0)
	# 	pen.write("PLAYER A WINS")
	# elif (score_b == 10):
	# 	wind.clear()
	# 	pen