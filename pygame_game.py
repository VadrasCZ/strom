import turtle as t

t.colormode(255)  # Allow RGB values from 0 to 255

# Funkce vykresli parez
def create_parez():
    t.fillcolor((139, 69, 19))  # A brownish color for the "parez" (stump)
    t.begin_fill()
    t.setheading(90)
    for _ in range(4):
        t.forward(90)
        t.right(90)
    t.end_fill()  # Called after the shape is completed

# Funkce vykresli listy
def create_listy():
    t.fillcolor((69, 140, 3))
    t.begin_fill()
    t.penup()
    t.goto(0, 90)
    t.pendown()
    t.left(90)
    t.forward(45)
    t.right(135)
    t.goto(45, 300)
    t.goto(135, 90)
    t.goto(0, 90)
    t.end_fill()

    
# Create the drawing
create_parez()
create_listy()

t.mainloop()
