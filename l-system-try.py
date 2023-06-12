from collections import deque
import string
import turtle

def lSysGenerate(s, order):
    for i in range(order):
        s = lSysCompute(s)
    return s

def lSysCompute(s):
    new = ""
    for c in s:
        if c == "X":
            new += "F[+X][-X]FX"
        elif c == "F":
            new += "FF"
        else:
            new += c
    return new

# def lSysCompute(s):
#     d = {"F": "F[+F]F[-F]F"}
#     d = {"F": "F[+F]F[-F][F]"}
#     d = {"F": "F[+F]F[-F]F"}
#     return ''.join([d.get(c) or c for c in s])

def draw(t, s, length, angle):
    stack = deque()
    for c in s:
        if c in string.ascii_letters:
            t.forward(length)
            # if c == "X":
            #     t.penup()
            #     t.forward(length)
            #     t.pendown()
            # elif c == "F":
            #     t.forward(length)
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
    # t.shape("turtle")
    t.hideturtle()

    t.left(90)
    t.pensize(1)
    t.penup()
    t.setpos(0, -300)
    t.pendown()
    t.speed(0)

    axiom = 'X'
    length = 1
    angle = 25.7
    iterations = 7


    s = lSysGenerate(axiom, iterations)
    # print(s)
    draw(t, s, length, angle)

    wn.exitonclick()

main()
# new = ""
# for c in "X[+F][-F]XF":
#     if c == "X":
#         new += "X[+F][-F]XF"
#     elif c == "F":
#         new += "FF"
#     else:
#         new += c

# print(new)