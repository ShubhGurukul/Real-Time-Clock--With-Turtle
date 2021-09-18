import turtle

turtle.pensize(5)
turtle.mode('logo')
turtle.speed(0)


# For hand Backlength from center
def jump(distance, store=0):
    turtle.penup()
    turtle.right(store)
    turtle.forward(-distance*.15)
    turtle.left(store)
    turtle.pendown()

# Draw hand
def hand(length, top):
    turtle.forward(length*1.15)
    turtle.right(90)
    turtle.forward(top/2.0)
    turtle.left(120)
    turtle.forward(top)
    turtle.left(120)
    turtle.forward(top)
    turtle.left(120)
    turtle.forward(top/2.0)

# make hand shape for all hands
def make_hand_shape(name, length, top):
    turtle.reset()
    jump(length)
    turtle.begin_poly()
    hand(length, top)
    turtle.end_poly()
    hand_shape = turtle.get_poly()
    turtle.register_shape(name, hand_shape)


# Draw Clock face
def draw_clockFace(radius):
    turtle.reset()
    
    turtle.penup()
    turtle.left(90)
    turtle.goto(0,radius)
    turtle.color('deepskyblue', 'orange')
    
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    # Inner Part of Watch
    turtle.goto()
    
    turtle.pensize(10)
    turtle.pencolor("red")
    turtle.penup()
    turtle.home()
    for i in range(12):
        turtle.penup()
        turtle.right(30)
        turtle.goto(0,0)
        turtle.forward(200)
        turtle.pendown()
        turtle.forward(25)

        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.write(str(i+1),align="center",font=("Arial", 18,"bold"))

# draw_clockFace(300)




def setup():
    global second_hand, minute_hand, hour_hand, writer
    make_hand_shape('second_hand', 120, 25)
    make_hand_shape('minute_hand', 135, 35)
    make_hand_shape('hour_hand', 90, 25)
    draw_clockFace(300)
    
    second_hand = turtle.Turtle()
    second_hand.shape('second_hand')
    second_hand.color("gray20", "gray80")

    minute_hand = turtle.Turtle()
    minute_hand.shape('minute_hand')
    minute_hand.color('orange','red2')


    hour_hand = turtle.Turtle()
    hour_hand.shape('hour_hand')
    hour_hand.color('blue3','deepskyblue')
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode('user')
        hand.shapesize(1,1,3)
        hand.speed(0)
    turtle.hideturtle()
    writer = turtle.Turtle()
    #writer.mode("logo")
    writer.hideturtle()
    writer.penup()
    writer.backward(85)


def weekday(t):
    weekday = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday[t.weekday()]

def date(z):
    month = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    j = z.year
    m = month[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)




def tick():
    t = datetime.today()

    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    
    turtle.tracer(False)
    writer = turtle.Turtle()
    writer.clear()
    writer.home()
    writer.penup()
    writer.forward(65)
    writer.pendown()
    writer.write(weekday(t),align="center", font=("Courier", 14, "bold"))
    writer.penup()
    writer.backward(150)
    writer.pendown()
    writer.write(date(t),align="center", font=("Courier", 14, "bold"))
    writer.penup()
    writer.forward(85)
    writer.pendown()
    turtle.tracer(True)
    
    second_hand.setheading(second*6)
    minute_hand.setheading(minute*6)
    hour_hand.setheading(hour*30)

    turtle.ontimer(tick, 100)
    
    
# setup()
# tick()    


def main():
    turtle.tracer(False)
    setup()
    turtle.tracer(True)
    tick()
    # return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    # print(msg)
    # mainloop()
    turtle.mainloop()
