from turtle import*

def draw_square (length, square_color):
    speed(5)
    color(square_color)
    for j in range(4):
        forward(length)
        right(90)
    mainloop()


for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

