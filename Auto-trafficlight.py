
import turtle

scr = turtle.Screen()
light = turtle.Turtle()

def init_graphics():
	# --- Init screen --- 
	scr.bgcolor("medium violet red")

	# --- draw housing ---
	light.penup()
	light.goto(-50, -50)
	light.pendown()
	light.fillcolor("grey")
	light.begin_fill()
	light.forward(100)
	light.left(90)
	light.forward(300)
	light.circle(50, 180)
	light.forward(300)
	light.left(90)
	light.end_fill()

	# poisition turtle
	light.penup()
	light.forward(50)
	light.left(90)
	light.forward(80)

	# Make green
	light.shape("circle")
	light.color("green")
	light.shapesize(4)

state = 0

def change_state():
    global state
    if state == 0:
    	light.ht()
    	light.forward(90)
    	light.color("orange")
    	light.st()
    	state = 1
    	scr.ontimer(change_state, "2000")
    elif state == 1:
    	light.ht()
    	light.forward(90)
    	light.color("red")
    	light.st()
    	state = 2
    	scr.ontimer(change_state, "5000")
    elif state == 2: 
    	light.ht()
    	light.backward(180)
    	light.color("green")
    	light.st()
    	state = 0
    	scr.ontimer(change_state, "10000")


init_graphics()
scr.onkey(change_state, "space")
scr.listen()


scr.mainloop()

"""
   session 14:34 --

"""