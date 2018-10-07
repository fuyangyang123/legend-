import turtle
def drawSnake(rad,angle,len,neckrad):
    colors = ["red","orange","yellow","green","cyan","blue"]
    for i in range(len):
        turtle.color(colors[i])
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.color("purple")
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
def main():
    turtle.setup(1300,800,0,0)
    turtle.penup()
    turtle.goto(-350,0)
    turtle.pendown()
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawSnake(40,80,6,pythonsize/2)
    main()
