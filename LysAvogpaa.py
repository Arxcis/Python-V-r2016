#!/usr/bin/python
# coding: utf-8

from turtle import Screen
from turtle import Turtle

s = Screen()
s.bgcolor('black')

ikea_lys = Turtle()
bestemors_lys = Turtle()

ikea_lys.shape('circle')
ikea_lys.color('black')
ikea_lys.shapesize(3)
bestemors_lys.shape('circle')
bestemors_lys.color('black')
bestemors_lys.shapesize(3)

class Lampe():
	lyser = False
	turtle = None


	def lag_skilpadde(self):
		""" Lager en egen skilpadde for denne lamen."""
		self.turtle = Turtle()
		self.turtle.penup()
		self.turtle.hideturtle()

		# Gult lys når vi lyser.
		self.turtle.shape('circle')
		self.turtle.color('yellow')
		self.turtle.shapesize(5)



	def slaa_paa(self):
		self.lyser = True
		self.turtle.showturtle()


	def slaa_av(self):
		self.lyser = False
		self.turtle.hideturtle()


#Lager lamper
a = Lampe()
b = Lampe()

# Lager skilpadder
a.lag_skilpadde()
b.lag_skilpadde()

a.turtle.forward(100)
b.turtle.backward(100)

#Skru på B


def ff_pa_aav(tut, paa_av):
	def factory_slaa():
		def slaa():
			tut.slaa_ + 'paa_av'+ ()
		return slaa_ + 'paa_av'
	

s.onkey(ff_pa_aav(a, 'paa'), 'a')
s.onkey(ff_pa_aav(a, 'av'), 'z')

s.onkey(ff_pa_aav(b, 'paa'), 's')
s.onkey(ff_pa_aav(b, 'av'), 'x')
s.listen()

s.mainloop()