"""
    Oppgave: 5.12 How to think like a computer scientist

    session 22:30 - 23:15
"""

from turtle import *

t = Turtle()
s = Screen()

# --- init screen ---
s.bgcolor("grey")

# --- Init turtle ---
t.color("yellow")
t.penup()
t.speed(0)
t.fillcolor("red")

# --- Variables ---
start_x = -300
start_y = -100
vekt_progresjon = [110, 130, 200, 240, 280, 320, 300, 290]


# --- Functions
def draw_soyle(vekt):
    t.begin_fill()
    t.pendown()
    t.forward(vekt)
    t.rt(90)
    t.write("     " + str(vekt), move=False, align="center", font=("Arial", 14, "italic"))
    t.fd(30)
    t.rt(90)
    t.fd(vekt)
    t.end_fill()
    t.penup()
    t.lt(90)
    t.fd(30)
    t.lt(90)


def draw_koordinatsystem():
    t.setpos(start_x + (len(vekt_progresjon * 60) + 30), start_y)
    t.write("Time", move=False, align="left", font=("Arial", 14, "italic"))
    t.seth(180)
    t.pendown()
    t.fd(len(vekt_progresjon)*60 + 30)
    t.rt(90)
    t.fd(300)
    t.write("Kilograms", move=False, align="center", font=("Arial", 14, "italic"))
    t.penup()


def draw_graph():
    t.setpos((start_x + 30), start_y)
    t.seth(90)
    for i in vekt_progresjon:
        draw_soyle(i)


draw_graph()
draw_koordinatsystem()
s.mainloop()