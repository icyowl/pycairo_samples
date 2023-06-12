from collections import deque
import string
import turtle

def lSysGenerate(s, order):
    for i in range(order):
        s = lSysCompute(s)
    return s

def lSysCompute(s):
    d = {
        "X": "F[+X][-X]FX",
        "F": "FF"
    }
    d = {
        "X": "F[+F][-F]FX",
        "F": "FF"
    }
    # d = {"F": "F[+F]F[-F]F"}
    return ''.join([d.get(c) or c for c in s])

def draw(t, s, length, angle):
    stack = deque()
    for c in s:
        if c in string.ascii_letters:
            t.forward(length)
        elif c == '-':
            t.left(angle)
        elif c == '+':
            t.right(angle)
        elif c == "[":
            agl = t.heading()
            pos = [t.xcor(), t.ycor()]
            stack.append((agl, pos))
        elif c == "]":
            agl, pos = stack.pop()
            t.setheading(agl)
            t.penup()
            t.goto(pos[0], pos[1])
            t.pendown()

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor('black')
    t.color('lightgreen')
    t.hideturtle()

    t.left(90)
    t.pensize(1)
    t.penup()
    t.setpos(0, -300)
    t.pendown()
    t.speed(0)

    axiom = 'X'
    length = 5
    angle = 25.7
    iterations = 5

    s = lSysGenerate(axiom, iterations)
    draw(t, s, length, angle)

    wn.exitonclick()

if __name__ == "__main__":

    main()

    # t = turtle.Turtle()
    # wn = turtle.Screen()
    # print(wn.window_width(), wn.window_height()) # -> 960 810