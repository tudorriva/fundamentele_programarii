import turtle


def rechteck(breite, hohe):
    for i in range(2):
        turtle.forward(breite)
        turtle.left(90)
        turtle.forward(hohe)
        turtle.left(90)


def d_rechteck(a_breite, a_hohe, i_breite, i_hohe):
    turtle.penup()
    turtle.goto(-a_breite / 2, -a_hohe / 2)
    turtle.pendown()
    rechteck(a_breite, a_hohe)


    turtle.penup()
    turtle.goto(-i_breite / 2, -i_hohe / 2)
    turtle.pendown()
    rechteck(i_breite, i_hohe)

    turtle.done()

def herz():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.left(140)
    turtle.forward(224)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)

    turtle.left(120)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)

    turtle.done()


def hauser():
    pen = turtle.Pen()
    pen2 = turtle.Pen()

    pen2.penup()
    pen2.goto(-310,0)
    pen2.pendown()

    #base
    for i in range(4):
        pen.forward(300)
        pen2.forward(300)

        pen.right(90)
        pen2.right(90)

    #roof
    pen.left(45)
    pen2.left(45)

    while int(pen.xcor()) < 150:
        pen.forward(5)
        pen2.forward(5)

    pen.right(90)
    pen2.right(90)

    while int(pen.ycor()) > 0:
        pen.forward(5)
        pen2.forward(5)


    #door
    pen.penup()
    pen2.penup()

    pen.goto(140,-300)
    pen2.goto(-165,-300)

    pen.pendown()
    pen2.pendown()

    pen.left(135)
    pen2.left(135)
    pen.forward(70)
    pen2.forward(70)
    pen.right(90)
    pen2.right(90)
    pen.forward(40)
    pen2.forward(40)
    pen.right(90)
    pen2.right(90)
    pen.forward(70)
    pen2.forward(70)
    
    #window
    pen.penup()
    pen2.penup()
    pen.goto(140,-150)
    pen2.goto(-165,-150)
    pen.pendown()
    pen2.pendown()

    pen.right(180)
    pen2.right(180)

    for i in range(4):
        pen.forward(40)
        pen2.forward(40)
        pen.right(90)
        pen2.right(90)

    turtle.done()

def menu():
    return """
            Wahlen Sie eine Zeichnung aus:
            1. Rechteck
            2. Herz
            3. Hauser
            0. Exit
            """

def main():
    while True:
        print(menu())
        opt = int(input('Zeichnung - '))
        if opt == 1:
           d_rechteck(200, 100, 50, 25)

        if opt == 2:
            herz()

        if opt == 3:
            hauser()

        if opt == 0:
            break



#hauser()
#d_rechteck(200, 100, 50, 25)
#herz()

main()

