"""
	Oppgave 5.146, s.68
	 session 00:20 - 00:36

"""
def grade_students():
	points = [83, 75, 74.9, 70, 69.9, 
		      65, 59.9, 55, 50, 49.9, 
		      45, 44.9, 40, 39.9, 2, 0]


	for i in points:
		i = float(i)
		poeng = str(i) + " pts. --> "
		if i >= 75:
			print(poeng + "First")
		elif 75 > i >= 70:
			print(poeng + "Upper second")
		elif 70 > i >= 60:
			print(poeng + "Second")
		elif 60 > i >= 50:
			print(poeng + "Third")
		elif 50 > i >= 45:
			print(poeng + "F1 Supp ")
		elif 45 > i >= 40: 
			print(poeng + "F2 ")
		elif 40 > i: 
			print(poeng + "F3 ")

grade_students()
input()