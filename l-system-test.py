import string
import turtle

def lSysGenerate(s, order):
    for i in range(order):
        s = lSysCompute(s)
    return s

def lSysCompute(s):
    # d = {'F': 'F-F++F-F'}
    d = {"F": "F+F-F-F+F"}
    return ''.join([d.get(c) or c for c in s])

def draw(t, s, length, angle):
    for c in s:
        if c in string.ascii_letters:
            t.forward(length)
        elif c == '-':
            t.left(angle)
        elif c == '+':
            t.right(angle)

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('black')

    t.color('lightgreen')
    t.pensize(1)
    t.penup()
    t.setpos(-250, 250)
    t.pendown()
    t.speed(0)

    axiom = 'F'
    length = 3
    angle = 90
    iterations = 4

    draw(t, lSysGenerate(axiom, iterations), length, angle)

    wn.exitonclick()

main()

