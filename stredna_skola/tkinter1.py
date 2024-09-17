import tkinter
import time


canvas = tkinter.Canvas(width = 400, height = 400, bg = "white")
canvas.pack()

def neutral():
    canvas.create_rectangle(50, 50, 130, 270, fill = "grey")
    canvas.create_oval(60, 60, 120, 120)
    canvas.create_oval(60, 130, 120, 190)
    canvas.create_oval(60, 200, 120, 260)


    canvas.create_rectangle(50, 50, 130, 270, fill = "grey")
    canvas.create_oval(60, 60, 120, 120, fill = "red")
    canvas.create_oval(60, 130, 120, 190)
    canvas.create_oval(60, 200, 120, 260)
    canvas.update()
    time.sleep(1.0)


    canvas.create_rectangle(50, 50, 130, 270, fill = "grey")
    canvas.create_oval(60, 60, 120, 120, fill = "red")
    canvas.create_oval(60, 130, 120, 190, fill = "yellow")
    canvas.create_oval(60, 200, 120, 260)
    canvas.update()
    time.sleep(1.0)
    
    
    canvas.create_rectangle(50, 50, 130, 270, fill = "grey")
    canvas.create_oval(60, 60, 120, 120)
    canvas.create_oval(60, 130, 120, 190)
    canvas.create_oval(60, 200, 120, 260, fill = "green")
    canvas.update()
    time.sleep(1.0)

while True:
    neutral()
