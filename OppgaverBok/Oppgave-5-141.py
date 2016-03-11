"""
	Oppgave 5.141
	Lag et program som input et tall mellom 0-6 fra brukeren, 
	og returnerer en string med hvilken dag det er. 

	session 23:19 - 22:35
"""

import easygui as box

def konvert_tall_dag():
	dag_int = box.integerbox("Skriv inn et tall mellom 0-6", "Hvilken dag er det?")
	dag_dict = {0:"Mandag", 1:"Tirsdag", 2:"Onsdag", 3:"Torsdag", 4:"Fredag", 5:"Lørdag", 6:"Søndag"}

	box.msgbox("Tallet du putta inn tilsvarer: %s" % dag_dict[dag_int], "Hvilken dag er det?")
	konvert_tall_dag()

konvert_tall_dag()