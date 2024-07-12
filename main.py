from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Main screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Turns off automatic screen updates for manual control

# Creating paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# Creating the ball
ball = Ball()

# Creating the scoreboard
scoreboard = Scoreboard()

# Setting up paddle controls
screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

# Main game loop
game_is_on = True
while game_is_on:
   time.sleep(ball.move_speed)
   ball.move()
   screen.update()

   # Detecting collision with top/bottom walls
   if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce_y()

   # Detecting collision with the right paddle
   if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
      ball.bounce_x()

   # Detecting collision with the left paddle
   if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
      ball.bounce_x()

   # Detecting right paddle scoring
   if ball.xcor() > 400:
      ball.restart_ball_position()
      scoreboard.left_paddle_point()

   # Detecting left paddle scoring
   if ball.xcor() < -400:
      ball.restart_ball_position()
      scoreboard.right_paddle_point()

# Keeps the window open until clicked
screen.exitonclick()
