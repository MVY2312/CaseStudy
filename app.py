import turtle
import tkinter as tk
import time

if __name__ == "__main__":
    #    turtle.penup()
    #   turtle.goto(-100, 200)
    #  turtle.pendown()
    # turtle.write('Фигура 1')

    turtle.penup()
    turtle.goto(-100, 180)
    turtle.pendown()
    turtle.fillcolor("#8B4513")
    turtle.begin_fill()
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

    # жираф
    turtle.fillcolor("#FFD700")
    turtle.begin_fill()

    turtle.right(60)
    turtle.forward(20)

    turtle.left(40)
    turtle.forward(30)

    turtle.left(50)
    turtle.forward(15)

    turtle.left(90)
    turtle.forward(45)

    turtle.right(90)
    turtle.forward(150)

    turtle.left(35)
    turtle.forward(60)

    turtle.right(35)
    turtle.forward(90)

    turtle.left(90)
    turtle.forward(30)

    turtle.left(90)
    turtle.forward(90)

    turtle.right(90)
    turtle.forward(45)

    turtle.left(90)
    turtle.forward(25)

    turtle.left(180)
    turtle.forward(25)

    turtle.left(45)
    turtle.forward(40)

    turtle.right(45)
    turtle.forward(60)

    turtle.left(90)
    turtle.forward(30)

    turtle.left(90)
    turtle.forward(140)

    turtle.right(145)
    turtle.forward(30)

    turtle.right(180)
    turtle.forward(80)

    turtle.left(55)
    turtle.forward(90)

    turtle.right(55)
    turtle.forward(60)

    turtle.right(35)
    turtle.forward(93)

    turtle.end_fill()
    turtle.pendown()

    # глаз

    turtle.penup()
    turtle.goto(-110, 160)
    turtle.fd(10); turtle.dot(10, "black");

    # sun
    turtle.penup()
    turtle.goto(180, 130)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    c = 0
    while True:
        c += 1
        turtle.pendown()
        turtle.forward(200)
        turtle.left(170)
        if c > 36:
            break
    turtle.end_fill()
    turtle.done()

    turtle.mainloop()
    #time.sleep(10)
