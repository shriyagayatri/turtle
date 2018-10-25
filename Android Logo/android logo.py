import turtle
turtle.speed(3)
turtle.bgcolor("black")


def head():
    turtle.color("green")
    turtle.fd(160)
    x = turtle.xcor()
    turtle.seth(90)
    turtle.begin_fill()
    turtle.circle(x / 2, 180)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(33, 37)
    turtle.pendown()
    turtle.dot(13, "black")
    turtle.penup()
    turtle.goto(126, 37)
    turtle.pendown()
    turtle.dot(13, "black")
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.hideturtle()
    turtle.fd(160)
    turtle.seth(90)
    turtle.circle(x / 2, 60)
    turtle.right(90)
    turtle.pensize(5)
    turtle.fd(30)

    turtle.penup()
    turtle.home()
    turtle.hideturtle()
    turtle.fd(160)
    turtle.seth(90)
    turtle.circle(x / 2, 120)
    turtle.right(90)
    turtle.pensize(5)
    turtle.pendown()
    turtle.fd(30)
    turtle.penup()
    turtle.home()
    turtle.penup()


def body():
    turtle.pensize(0)
    turtle.home()
    turtle.showturtle()
    turtle.goto(0, -7)
    turtle.pendown()
    turtle.begin_fill()
    for m in range(2):
        turtle.fd(160)
        turtle.right(90)

    turtle.fd(160)
    turtle.right(90)
    turtle.fd(120)
    turtle.end_fill()


def legs():
    turtle.penup()
    turtle.goto(33, -169)
    turtle.pendown()
    turtle.pensize(32)
    turtle.fd(43)
    turtle.penup()
    turtle.goto(130, -169)
    turtle.pendown()
    turtle.fd(43)
    turtle.penup()


def hands():
    turtle.home()
    turtle.pensize(30)
    turtle.goto(-18, -77)
    turtle.pendown()
    turtle.left(90)
    turtle.fd(65)
    turtle.penup()
    turtle.goto(179, -77)
    turtle.pendown()
    turtle.fd(65)
    turtle.penup()
    turtle.hideturtle
    turtle.fd(100)
    turtle.hideturtle()
    turtle.circle(100)
    turtle.circle(100, 360, 59)


head()
body()
legs()
hands()