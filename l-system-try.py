from collections import deque
import string
import turtle

def lSysGenerate(s, order):
    for i in range(order):
        s = lSysCompute(s)
    return s

def lSysCompute(s):
    # d = {'F': 'F-F++F-F'}
    d = {"F": "F[+F]F[-F]F"}
    return ''.join([d.get(c) or c for c in s])

def draw(t, s, length, angle):
    stack = deque()
    t.left(90)
    for c in s:
        if c in string.ascii_letters:
            t.forward(length)
        elif c == '-':
            t.left(angle)
        elif c == '+':
            t.right(angle)
        elif c == "[":
            _angle = t.heading()
            pos = [t.xcor(), t.ycor()]
            stack.append((_angle, pos))
        elif c == "]":
            _angle, pos = stack.pop()
            t.setheading(_angle)
            t.penup()
            t.goto(pos[0], pos[1])
            t.pendown()

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('black')

    t.color('lightgreen')
    t.pensize(1)
    t.penup()
    t.setpos(0, -250)
    t.pendown()
    t.speed(0)

    axiom = 'F'
    length = 10
    angle = 30
    iterations = 3

    draw(t, lSysGenerate(axiom, iterations), length, angle)

    wn.exitonclick()

main()