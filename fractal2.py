import turtle


turtle.speed(100)
turtle.tracer(0)
turtle.hideturtle()
turtle.penup()
turtle.setx(-400)
turtle.sety(-200)
turtle.pendown()



axiom = "a"
axmTemp = ""
itr = 9

dl = 1
angl = 60

translate = {"+":"+", "-":"-", "a":"b-a-b", "b":"a+b+a"}
for k in range(itr):
	for ch in axiom:
		axmTemp += translate[ch]
	axiom = axmTemp
	axmTemp = ""

turtle.fillcolor("black")
turtle.begin_fill()

for ch in axiom:
	if ch == "+":
		turtle.right(angl)
	elif ch == "-":
		turtle.left(angl)

	else:
		turtle.forward(dl)
turtle.update()
turtle.end_fill()
turtle.done()


