import turtle

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setpos(-100, -150)
turtle.pendown()



axiom = "FX"
axmTemp = ""
itr = 15

dl = 1.2
angl = 90

translate = {"+":"+", "-":"-", "F":"F", "X":"X+YF+", "Y":"-FX-Y"}
for k in range(itr):
	for ch in axiom:
		axmTemp += translate[ch]
	axiom = axmTemp
	axmTemp = ""

# turtle.fillcolor("black")
# turtle.begin_fill()

for ch in axiom:
	if ch == "+":
		turtle.right(angl)
	elif ch == "-":
		turtle.left(angl)

	else:
		turtle.forward(dl)
turtle.update()
# turtle.end_fill()
turtle.done()


