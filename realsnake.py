from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('black')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen, body):
    super().__init__()
    self.alive = True
    self.speed(0)
    self.shape("square")
    self.color("black")
    self.penup()
    self.goto(0,0)

    self.direction = ("up", "down", "left", "right")
    screen.onkeypress(self.up, "Up")
    screen.onkeypress(self.down, "Down")
    screen.onkeypress(self.left, "Left")
    screen.onkeypress(self.right, "Right")


  def up(self):
    if self.direction != "down":
      self.direction = "up"
      self.setheading(90)


  def down(self):
    if self.direction != "up":
      self.direction = "down"
      self.setheading(-90)

  def left(self):
    if self.direction != "right":
      self.direction = "left"
      self.setheading(180)

  def right(self):
    if self.direction != "left":
      self.direction = "right"
      self.setheading(0)

  def move(self):
    self.forward(20)
    if self.xcor() > 240 or self.xcor()< -240 or self.ycor() > 240 or self.ycor() < -240:
      self.alive = False 


  def die(self):
    if self.alive == False:
      head.hideturtle()
      
class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.ht()
    self.speed(0)
    self.shape("square")
    self.color("green")
    self.penup()
    self.goto(other.xcor(),other.ycor())
    self.st()
    

  def move(self, other):
    self.goto(other.xcor(),other.ycor())

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.speed(0)
    self.shape("circle")
    self.color("red")
    self.penup()
    self.goto(100,100)

  def relocate(self):
      x = random.randint(-230,230)
      y = random.randint(-230,230)
      self.goto(x,y)

def update():
  if p1.alive == True:
    p1.move()

    # moves the snake body
    for i in range(len(body) -1, 0, -1):
      body[i].move(body[i - 1])

    # Collision detection
    if p1.distance(apple) < 20:
      apple.relocate()
      body.append(Segment(body[-1]))


   


    


  screen.ontimer(update, 120)


#####################################################################################################################################################################################

screen = Screen()
screen.bgcolor("lime green")
screen.setup(520,520)
screen.listen()
screen.onkey(update, "space")



body = [] 


p1 = Head(screen, body)
body.append(p1)
body.append(Segment(body[-1]))
body[1].color("black")
apple = Apple()





screen.exitonclick()
