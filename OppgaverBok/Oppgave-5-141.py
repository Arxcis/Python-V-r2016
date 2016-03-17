"""
	Oppgave 5.141 og 5.142
	Lag et program som input et tall mellom 0-6 fra brukeren, 
	og returnerer en string med hvilken dag det er. 

	session 23:50 - 00:11
	session 23:19 - 22:35
"""

import easygui as box

dag_dict = {0:"Mandag", 
			1:"Tirsdag",
			2:"Onsdag",
			3:"Torsdag",
			4:"Fredag",
			5:"Lørdag",
			6:"Søndag"}

def konvert_tall_dag():
	dag_int = box.integerbox("Hvilken ukedag skal du inn i fengsel?", "Hvilken dag er det?")
	dag_int -= 1
	box.msgbox("Tallet du putta inn tilsvarer: %s" % dag_dict[dag_int], "Hvilken dag er det?")
	dager_i_fengsel(dag_int)


def dager_i_fengsel(ukedag):
	antall = int(box.enterbox("Hvor mange dager skal du være i fengsel?", "Hilken dag er det?"))
	cache = int(ukedag)
	for i in range(antall):
		if cache < 6:
			cache += 1
		else:
			cache = 0
	box.msgbox("Etter å ha vært i fengsel i %d dager, så kommer du til å slippe ut på en %s" % (antall, dag_dict[cache]))

konvert_tall_dag()


