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
    pass


# Draw Clock face
def draw_clockFace(radius):
    pass




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
