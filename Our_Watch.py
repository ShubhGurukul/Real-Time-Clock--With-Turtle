import turtle
from datetime import datetime


# turtle.speed(0)
# turtle.shapesize(5,5,5)
# for i in range(60):
#     turtle.left(6)

turtle.pensize(4)

def hand(length, top):
    turtle.begin_poly()
    turtle.forward(length*1.15)
    turtle.right(90)
    turtle.forward(top/2.0)
    turtle.left(120)
    turtle.forward(top)
    turtle.left(120)
    turtle.forward(top)
    turtle.left(120)
    turtle.forward(top/2.0)
    turtle.end_poly()

hand(125, 25)
minute = turtle.get_poly()
minute_hand = turtle.register_shape("minute", minute)

turtle.shape("minute")
turtle.resetscreen()
sec = datetime.today().second
turtle.left(180- sec*6)
turtle.resizemode("user")
turtle.turtlesize(2, 2, 5)
turtle.color('red', 'blue')
def tick():
    turtle.right(6)
    turtle.ontimer(tick, 1000)

turtle.ontimer(tick, 1000)





turtle.mainloop()

'''
turtle.left(180)
turtle.fd(90)
turtle.backward(180)

# hand(125, 25)
# turtle.goto(0,0)
# # turtle.left(90)
# hand(125,40)
# hand

'''