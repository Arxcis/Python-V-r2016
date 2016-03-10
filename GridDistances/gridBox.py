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
# scr.setup(830, 830)

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
    # --- Create a 5 X 5 grid, with positinal values, stored as a list ---
    for i in range(5):
        for j in range(5):
            extend_list = [-400 + (200*j), 400 - (200*i)]
            position_grid.extend(extend_list)
    print(position_grid)               # Debugging data
    print(len(position_grid))          # Debugging data


def show_positiongrid(method, submethod):
    global position_grid
    # ---- Display the 5 X 5 grid on screen ----
    for i in range(25):
        writer.setpos(position_grid[2*i], position_grid[(2*i)+1])

        # --- Get floater and writer position int form ---
        floater_x, floater_y = floater.position()
        floater_x = int(floater_x)
        floater_y = int(floater_y)
        writer_x, writer_y = writer.position()
        writer_x = int(writer_x)
        writer_y = int(writer_y)

        # --- Calculate distance for all points in grid ----
        d = int(math.sqrt(((floater_x - writer_x) ** 2) + ((floater_y - writer_y) ** 2)))
        
        # ---- Methods for displaying grid informatiion -----
        if method  == 1:
            #--- Method 1 ---  Print values in a grid, using writer.distance()-function
            writer.write(writer.distance(floater_x, floater_y))
            
        elif method == 2:
            # --- Method 2 ---  Print values in a grid, using "d"
            writer.write(d)
            
        elif method == 3:
            # --- Method 3 ---  Print values to console, no grid
            print(d)
            
        elif method == 4:
            # --- Method 4 ---  THE MOST AWESOME METHOD !
            colorpick = int(255/(d*0.01))
            if colorpick > 255:
                colorpick = 255
            else:
                pass
            writer.color(colorpick, 0, 0)
            if submethod == 1:
                # --- Method 4a ---
                writer.write(d)
            elif submethod == 2:
                # --- Method 4b ---
                writer.fillcolor((colorpick, 0, 0))
                writer.begin_fill()
                writer.circle(7)
                writer.end_fill()
        
        else:
            return print("Wrong input! to show_position()")


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
    # --- Constant movement of turtle ---
    floater.forward(3)

    # --- Statement is passed every 0.1 second ---
    if time.clock() > clock_cache + 0.1:
        writer.clear()
        show_positiongrid(4, 2)
        clock_cache = time.clock()

scr.mainloop()

