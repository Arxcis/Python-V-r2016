"""
    Tittel: gridBox -
    Opprettet: 10.03.2016 - kl 11:50
    Beskrivelse: Måle avstanden fra forskjellige punkter til en turtle

            12:29  13:28  Jonas
            11:52 12:25   Jonas
"""
import turtle
import time
import math

# --- Import objects ---
floater = turtle.Turtle()
writer = turtle.Turtle()
scr = turtle.Screen()


# --- Init Screen ---
scr.bgcolor("Black")
scr.delay(5)
scr.setup(900, 900)

# --- Init floater ----
floater.color("Green")
floater.shape("turtle")
floater.penup()
floater.speed(1)

# --- Init writer ---
writer.hideturtle()
writer.penup()
writer.color("White")
writer.speed(0)


# --- Variables ---
game_over = False
clock_cache = 0
position_grid = []


def create_positiongrid():
    global position_grid

    for i in range(5):
        for j in range(5):
            extend_list = [-400 + (200*j), 400 - (200*i)]
            position_grid.extend(extend_list)
    print(position_grid)               # Debugging data
    print(len(position_grid))          # Debugging data


def show_positiongrid():
    global position_grid
    for i in range(25):
        writer.setpos(position_grid[2*i], position_grid[(2*i)+1])
        # --- Get floater and writer position int form ---
        floater_x, floater_y = floater.position()
        floater_x = int(floater_x)
        floater_y = int(floater_y)
        writer_x, writer_y = writer.position()
        writer_x = int(writer_x)
        writer_y = int(writer_y)

        # --- Method 1 ---  Print values in a grid, using writer.distance()-function
        # writer.write(writer.distance(floater_x, floater_y))

        # --- Calculate distance for all points in grid ----
        d = int(math.sqrt(((floater_x - writer_x) ** 2) + ((floater_y - writer_y) ** 2)))

        # --- Method 2 ---  Print values in a grid, using "d"
        # writer.write(d)

        # --- Method 3 ---  Print values to console, no grid
        # print(d)

        # --- Method 4 ---  THE MOST AWESOME METHOD !
        colorpick = int(255/(d*0.005))
        if colorpick > 255:
            colorpick = 255
        else:
            pass
        writer.color(colorpick, 0, 0)
        writer.write(d)


def move_left():
    floater.left(30)


def move_right():
    floater.right(30)


# --- Main ---
scr.onkey(move_left, "Left")
scr.onkey(move_right, "Right")
scr.listen()


create_positiongrid()
scr.colormode(255)

while game_over is False:
    floater.forward(3)

    if time.clock() > clock_cache + 0.1:
        writer.clear()
        show_positiongrid()
        clock_cache = time.clock()

scr.mainloop()

