from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")

class Scoreboard(Turtle):

   def __init__(self):
      super().__init__()
      self.color("white")
      self.penup()
      self.hideturtle()
      self.r_score = 0
      self.l_score = 0
      self.goto(0, 250)
      self.update_scoreboard()
   
   def update_scoreboard(self):
      self.clear()
      self.write(f"{self.l_score} I {self.r_score}", align="center", font=FONT)

   def right_paddle_point(self):
      self.r_score += 1
      self.update_scoreboard()
   
   def left_paddle_point(self):
      self.l_score += 1
      self.update_scoreboard()
