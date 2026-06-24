# for i in range(11):
#     print('i`il become not russian')
# else:
#     print('пизда')
# n = int(input())
# for i in range(n):
#     print('анус')
# # Heart Drawing Code
import turtle

screen = turtle.Screen()
screen.title("Heart Drawing")

pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("pink")
pen.speed(5)

pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

pen.hideturtle()
turtle.done()