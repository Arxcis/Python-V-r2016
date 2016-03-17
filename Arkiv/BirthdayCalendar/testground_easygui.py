"""
    Tittel: En kalender med turtle og easygui
    Opprettet: 23:49 - 10.03.16
        av Jonas Solsvik

    session 23:50 - 01:00
"""
import easygui as box
import sys
from turtle import *

t1 = Turtle()
scr = Screen()

# 1. Meldingsboks - viser melding med OK knapp (OK kan redigeres)
box.msgbox("Hello world")

# 2. Continue or cancel boks - samme som meldingsboks med Continue og Cancel knapp.
if box.ccbox("Which way do you want to go?", "The big choice"):   # 2. Continue or cancel"
    pass
else:
    sys.exit()

# - - Turtle kan fint blandes med easygui ----
t1.forward(90)

choices = ["Yes", "No", "Maybe"]

# 3. Buttonbox - Gir mulighet til flere knapper, som kan redigeres hver for seg.
#                Return --> Strengen som knappen viser.
answer = box.buttonbox("Do you want to continue", "Prompt", choices)

# 3. Dette behandler return fra buttonbox


def continue_program(a):
    while 1:
        if a == "Yes":
            break
        elif a == "No":
            sys.exit()
        elif a == "Maybe":

            box.msgbox("Make up your mind you damned fool!")
            a = box.buttonbox("Do you want to continue", "Prompt", choices)


continue_program(answer)
scr.bye()

# 1. Messagebox med endret ok_knapp
box.msgbox("Backup complete!", ok_button="Good job!")

# 4, 5 og 6 - inputbokser
box.enterbox("Enter your name: ", "Facebook")
box.integerbox("Enter your age: ", "Facebook")
box.multenterbox("More info: ", "Facebook", ["Your weight", "Your status", "your employment"])

# 7. Passordboks - Siste feltet blir regnet som passordfeletet
box.multpasswordbox("Insert username and password", "Facebook", ["Username: ", "Password: "])
