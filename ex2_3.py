import turtle as t
week = ['black','grey','darkgreen','gold','violet','purple','green','red']
def drawSnake(r,angle,length):
   t.seth(-40)
   for i in range(length):
       t.pencolor(week[i%8])
       t.circle(r,angle)
       t.pencolor(week[(i+1)%8])
       t.circle(-r,angle)
   t.circle(r,angle/2)
   t.fd(40)
   t.circle(16,180)
   t.fd(40*2/3)
t.setup(650,350)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
drawSnake(40,80,9)
t.done()
