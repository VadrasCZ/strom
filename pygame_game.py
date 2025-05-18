import turtle as t

t.colormode(255)  # Allow RGB values from 0 to 255

#Function that creates a tree
def create_strom(x, y):
    t.penup()
    t.fillcolor((139, 69, 19))
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(90)
    for i in range(4):
        t.forward(90)
        t.right(90)
    t.end_fill()

    t.fillcolor((27, 110, 7))
    t.begin_fill()
    t.goto(x, y + 90)
    t.goto(x - 45, y + 90)
    t.goto(x + 45, y + 325)    
    t.goto(x + 135, y + 90)
    t.goto(x + 90, y + 90)
    t.goto(x, y + 90)
    t.end_fill()

    

# Creating 5 trees 180 pixels between themselves
create_strom(-360, 0)
create_strom(-180, 0)
create_strom(0, 0)
create_strom(180, 0)
create_strom(360, 0)

t.mainloop()