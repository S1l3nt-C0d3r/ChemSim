import random
import turtle
from turtle import *
setup()

t = Turtle()

colors = ["yellow", "orange"]
t.up()
t.speed(0)
i=0
while i>-1:
 for i in range(0,5):
     x = random.randint(-10, 10)
     y = random.randint(-100, 100)
     circle_size = 10
     circle_color = random.choice(colors)
     t.goto(x, y)
     t.down()
     t.color(circle_color)
     t.begin_fill()
     t.circle(circle_size)
     t.end_fill()
     t.up()
     i+=1
     if i==5:
         t.clear()