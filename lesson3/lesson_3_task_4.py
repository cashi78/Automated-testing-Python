from turtle import Turtle

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(800, 600)
my_turtle.width(10)


# Нарисовать квадрат
def draw_rect(t):
    my_turtle.down()
    for x in range(0, 4):
        my_turtle.right(90)
        my_turtle.forward(t)
    my_turtle.up()


my_turtle.fillcolor("yellow")
my_turtle.begin_fill()
draw_rect(200)

my_turtle.goto(-200, 100)
draw_rect(140)
my_turtle.end_fill()
my_turtle.fillcolor("brown")
my_turtle.begin_fill()
my_turtle.goto(-200, 130)
draw_rect(30)
my_turtle.end_fill()
my_turtle.goto(-310, 130)
draw_rect(30)
my_turtle.goto(-260, 30)
draw_rect(30)
my_turtle.goto(-290, 80)
draw_rect(20)
my_turtle.goto(-220, 80)
draw_rect(20)
my_turtle.goto(-200, -200)
draw_rect(30)
my_turtle.goto(-150, -200)
draw_rect(30)
my_turtle.goto(-50, -200)
draw_rect(30)
my_turtle.goto(0, -200)
draw_rect(30)
my_turtle.goto(30, 30)
draw_rect(30)


# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()
