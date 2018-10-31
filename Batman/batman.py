import turtle
import math

Pen = turtle.Turtle()
Pen.speed(500)
Pen.pensize(8)

window = turtle.Screen()
window.bgcolor("black")
Pen.color("red")

zoom = 80

Pen.left(90)
Pen.penup()
Pen.goto(-7 * zoom, 0)
Pen.pendown()

for xz in range(-7 * zoom, -3 * zoom, 1):
    x = xz / zoom
    absx = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(absx - 1)) * math.fabs(3 - absx) / ((absx - 1) * (3 - absx))) * (
                1 + math.fabs(absx - 3) / (absx - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - absx) / (1 - absx))
    Pen.goto(xz, y * zoom)

for xz in range(-3 * zoom, -1 * zoom - 1, 1):
    x = xz / zoom
    absx = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * absx - 1.35526 * math.sqrt(4 - (absx - 1) ** 2)) * math.sqrt(
        math.fabs(absx - 1) / (absx - 1))
    Pen.goto(xz, y * zoom)

Pen.goto(-1 * zoom, 3 * zoom)
Pen.goto(int(-0.5 * zoom), int(2.2 * zoom))
Pen.goto(int(0.5 * zoom), int(2.2 * zoom))
Pen.goto(1 * zoom, 3 * zoom)

for xz in range(1 * zoom + 1, 3 * zoom + 1, 1):
    x = xz / zoom
    absx = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * absx - 1.35526 * math.sqrt(4 - (absx - 1) ** 2)) * math.sqrt(
        math.fabs(absx - 1) / (absx - 1))
    Pen.goto(xz, y * zoom)

for xz in range(3 * zoom + 1, 7 * zoom + 1, 1):
    x = xz / zoom
    absx = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(absx - 1)) * math.fabs(3 - absx) / ((absx - 1) * (3 - absx))) * (
                1 + math.fabs(absx - 3) / (absx - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - absx) / (1 - absx))
    Pen.goto(xz, y * zoom)

for xz in range(7 * zoom, 4 * zoom, -1):
    x = xz / zoom
    absx = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(absx - 4) / (absx - 4))
    Pen.goto(xz, y * zoom)

for xz in range(4 * zoom, -4 * zoom, -1):
    x = xz / zoom
    absx = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(absx - 2) - 1) ** 2)
    Pen.goto(xz, y * zoom)

for xz in range(-4 * zoom - 1, -7 * zoom - 1, -1):
    x = xz / zoom
    absx = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(absx - 4) / (absx - 4))
    Pen.goto(xz, y * zoom)



Pen.penup()

Pen.hideturtle()
input()