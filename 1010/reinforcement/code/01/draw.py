import turtle

sam = turtle.Turtle()


def main():

    goto_start()
    square(10)

    sam.fd(200)

    star()

    # next row
    sam.rt(90)
    sam.fd(300)
    sam.rt(90)
    sam.fd(200)
    sam.rt(180)

    triangle()

    sam.fd(300)

    circleish()


def goto_start():
    sam.pu()
    sam.lt(90)
    sam.fd(200)
    sam.lt(90)
    sam.fd(200)
    sam.lt(180)


def square(length):
    length = 150
    angle = 72
    sam.pd()
    sam.fd(length)
    sam.rt(angle)
    sam.fd(length)
    sam.rt(angle)
    sam.fd(length)
    sam.rt(angle)
    sam.fd(length)
    sam.rt(angle)
    sam.fd(length)

    sam.pu()


def star():
    angle = 144
    length = 150
    sam.pd()
    sam.fd(length)
    sam.rt(angle)
    sam.fd(length)
    sam.rt(angle)
    sam.fd(length)
    sam.rt(angle)
    sam.fd(length)
    sam.rt(angle)
    sam.fd(length)
    sam.rt(angle)
    sam.pu()


def triangle():
    sam.fd(50)
    sam.pd()
    sam.rt(60)
    sam.fd(100)
    sam.rt(120)
    sam.fd(100)
    sam.rt(120)
    sam.fd(100)
    sam.rt(60)
    sam.pu()


def circleish():
    angle = 3.6
    length = 5
    sam.pd()
    for _ in range(100):
        sam.fd(length)
        sam.rt(angle)


main()
input()
