import turtle
import time
t = turtle.Pen()
for x in range(4):
	t.up()
	t.forward(25)
	t.down()
	t.forward(100)
	t.up()
	t.forward(25)
	t.down()
	t.left(90)
time.sleep(3)
