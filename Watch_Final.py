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
    pass

def weekday(t):
    pass


def date(z):
    pass




def tick():
    pass


def main():
    pass

if __name__ == "__main__":
    turtle.mainloop()
