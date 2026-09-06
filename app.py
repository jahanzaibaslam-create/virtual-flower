import turtle
import math
import random

screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("#09091a")
screen.title("A Rose For You 🌹")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw one petal
def petal(size, angle):
    t.begin_fill()

    for _ in range(30):
        t.forward(size / 30)
        t.left(angle / 30)

    for _ in range(30):
        t.forward(size / 30)
        t.left((180 - angle) / 30)

    t.end_fill()


# Rose head
t.penup()
t.goto(0, 100)
t.setheading(0)
t.pendown()

t.color("#ff1744")
t.fillcolor("#e91e63")

for i in range(18):

    petal(100, 70)

    t.left(20)


# Inner petals
t.penup()
t.goto(0, 100)
t.setheading(0)
t.pendown()

t.color("#ff4f81")
t.fillcolor("#ff1744")

for i in range(12):

    petal(65, 65)

    t.left(30)


# Center
t.penup()
t.goto(0, 100)
t.dot(30, "#ffd54f")


# Stem
t.penup()
t.goto(0, 100)
t.setheading(-90)
t.pendown()

t.pensize(12)
t.color("#2e7d32")

t.forward(280)


# Left leaf
t.penup()
t.goto(0, -40)
t.setheading(150)
t.pendown()

t.fillcolor("#43a047")
t.begin_fill()

for i in range(30):
    t.forward(3)
    t.right(3)

for i in range(30):
    t.forward(3)
    t.right(3)

t.end_fill()


# Right leaf
t.penup()
t.goto(0, -100)
t.setheading(30)
t.pendown()

t.fillcolor("#66bb6a")
t.begin_fill()

for i in range(30):
    t.forward(3)
    t.left(3)

for i in range(30):
    t.forward(3)
    t.left(3)

t.end_fill()


# Message
t.penup()
t.goto(0, -270)

t.color("#ffffff")

t.write(
    "A little rose, just for you 🌹❤️",
    align="center",
    font=("Georgia", 22, "italic")
)


screen.mainloop()