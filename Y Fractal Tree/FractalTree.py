import turtle
turtle.bgcolor('black')
turtle.color('white')
turtle.penup()
turtle.right(90)
turtle.forward(350)
turtle.left(180)
turtle.pendown()
turtle.speed(10)

def draw(l):
    if(l<10):
        return
    else:
        turtle.forward(l)
        turtle.left(30)
        draw(3*l/4)
        turtle.right(60)
        draw(3*l/4)
        turtle.left(30)
        turtle.backward(l)

draw(200)
turtle.exitonclick()
turtle.hideturtle()