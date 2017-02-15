#Import Libraries
import Tkinter    #Graphics
import tkFont     #Fonts

#Window Setup Variables
TITLE = "Drop the Box"
WIDTH = 640
HEIGHT = 480
RESOLUTION = str(WIDTH) + "x" + str(HEIGHT)

#Game Setup Variables
SPEED = 0.1
POINTS = 10
BOX_SIZE = 50
BOX_TOP = 50
BAR_THICK = 20
BAR_WIDTH = 80
BAR_HEIGHT = 80
BAR_POS1 = (WIDTH / 2) - (BAR_WIDTH / 2)
BAR_POS2 = (WIDTH / 2) + (BAR_WIDTH / 2)

#-------------------------------------------------------------------------

#Create a Window and Graphics Context
window = Tkinter.Tk()
window.title(TITLE)
window.geometry(RESOLUTION)
window.minsize(WIDTH, HEIGHT)
window.maxsize(WIDTH, HEIGHT)
canvas = Tkinter.Canvas(window)
canvas.config(width = WIDTH, height = HEIGHT)
canvas.pack()
canvas.master.geometry(RESOLUTION)

#Create Game Objects (Format: x1, y1, x2, y2, <option>=<value>, ...)
background = canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="black")
scorebar = canvas.create_rectangle(0, 0, WIDTH, 30, fill="blue")
scoretext = canvas.create_text(5, 0, text="Score: 0", fill="white",
                               anchor = Tkinter.NW,
                               font = tkFont.Font(size = -25))
box = canvas.create_rectangle(0, BOX_TOP, BOX_TOP + BOX_SIZE,
                                          BOX_TOP + BOX_SIZE, fill="cyan")
bar1 = canvas.create_rectangle(BAR_POS1 - BAR_THICK, HEIGHT - BAR_HEIGHT,
                               BAR_POS1, HEIGHT, fill="green")
bar2 = canvas.create_rectangle(BAR_POS2, HEIGHT - BAR_HEIGHT,
                               BAR_POS2 + BAR_THICK, HEIGHT, fill="green")

#-------------------------------------------------------------------------

#Game Global Variables
#(not usually recommended but required for persistence)
x = 0
y = BOX_TOP
speed = SPEED
state = 0
score = 0

#Main Program Loop and Game Logic
def main():
    global x, y, state, speed, score

    #Decide how the box will move on the screen
    if(state == 1): #Drop the box downwards into the container
        y = y + SPEED
        if(y > HEIGHT - BOX_SIZE):
            #Is the box in the container?
            if((x > BAR_POS1) and (x < BAR_POS2 - BOX_SIZE)):
                score = score + POINTS
                canvas.itemconfigure(scoretext,
                                     text = "Score: " + str(score))
            #Reset the box
            y = BOX_TOP
            state = 0

    else: #Move left to right continuously and bounce on the walls
        x = x + speed
        if(x > WIDTH - BOX_SIZE):
            x = WIDTH - BOX_SIZE
            speed = SPEED * -1
        elif(x < 0):
            x = 0
            speed = SPEED * 1

    #Update Positions of Game Objects
    canvas.coords(box, x, y, x + BOX_SIZE, y + BOX_SIZE)

    #Refresh the Screen
    canvas.update_idletasks()
    window.after(0, main)

#-------------------------------------------------------------------------

#Drop the Box
def drop(event):
    global state
    if(state == 0):
        state = 1

#Run the Main Program
print("Drop the Box!")
window.after(1, main)
window.bind("<space>", drop)
window.bind("<Return>", drop)
window.bind("<Button-1>", drop)
window.mainloop()
