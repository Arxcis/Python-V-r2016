"""
	Oppgåve 7-19, s.102
	03:10 - 04:12 - 27 min
"""
import easygui
import time

inn_tall = easygui.integerbox("Hvor stor gangetabell ønsker du ? \n\n "
	                           " Et tall mellom 0 og 40! ", "MULTGANGETABELL") 

def print_mutliples(tall, columns):
	global gangestring
	for i in range(1, columns + 1):
		if len(str(i*tall)) == 1:
			print(i * tall, end="   ")
			gangestring += (str(i * tall) + "      ")
		elif len(str(i*tall)) == 2: 
			print(i * tall, end="  ")
			gangestring += (str(i * tall) + "    ")
		else:
			print(i * tall, end=" ")
			gangestring += (str(i * tall) + " ")
	print()

def print_gangetabell(rows):
	global gangestring
	for i in range(1, rows + 1):
		print_mutliples(i, rows)
		gangestring += ("\n")


def format_clock(cpu_time):
	print("Clock2 - Clock 1 = : " + str(cpu_time))
	cpu_time = cpu_time * 1.0e4
	print("CPU-time * 10 000 = " + str(cpu_time))
	purge = cpu_time % 1.0    # This is where the magic happens :)
	print("This is behind the comma: " + str(purge))
	cpu_time = cpu_time - purge  
	print("This is what is left after the purge: " + str(cpu_time))
	cpu_time = cpu_time / 10
	print("This is in milliseconds: " + str(cpu_time))
	return cpu_time


gangestring = ""

clock1 = time.clock()        # Tidtaking punkt 1
print_gangetabell(inn_tall)
clock2 = time.clock()		 # Tidtaking punkt 2

cpu_time = clock2 - clock1
tid = format_clock(cpu_time)         

cpu_timestring = ("CPU time " + (str(tid)) + " ms !")

easygui.msgbox("Prosessoren brukte " + cpu_timestring, "MULTGANGETABELL")
gangestring = easygui.textbox(gangestring)