import turtle
import time
from math import*
screen=turtle.Screen()
screen.tracer(50)
sun=turtle.Turtle()
sun.shape('triangle')
sun.color('yellow')
class planet(turtle.Turtle):
    def __init__(self,name,radius,color):
        super().__init__(shape='triangle')
        self.name=name
        self.radius=radius
        self.c=color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle=0
    def move(self):
        x=self.radius*cos(self.angle)
        y=self.radius*sin(self.angle)
        self.goto(sun.xcor()+x,sun.ycor()+y)
mercury=planet("mercury",40,'grey')
venus=planet("venus",80,'orange')
earth=planet("earth",100,'blue')
mars=planet("mars",150,'brown')
jupiter=planet("jupiter",180,'light blue')
saturn=planet("saturn",230,'black')
uranus=planet("uranus",250,'pink')
neptune=planet("neptune",280,'red')
mylist=[mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
while True:
    screen.update()
    for i in mylist:
        i.move()
        mercury.angle+=0.002
        venus.angle+=0.002
        earth.angle+=0.002
        mars.angle+=0.002
        jupiter.angle+=0.002
        saturn.angle+=0.002
        uranus.angle+=0.002
        neptune.angle+=0.002
        
        
