import tkinter
import time
canvas = tkinter.Canvas(width = 800, height = 600, bg="white")
canvas.pack()

def semafor():
    canvas.create_rectangle(50, 50, 200, 480, fill="grey")
    canvas.create_oval(60, 60, 190, 190, fill="white")
    canvas.create_oval(60, 200, 190, 330, fill="white")
    canvas.create_oval(60, 340, 190, 470, fill="white")
    time.sleep(1)

def red():
    canvas.create_rectangle(50, 50, 200, 480, fill="grey")
    canvas.create_oval(60, 60, 190, 190, fill="red")
    canvas.create_oval(60, 200, 190, 330, fill="white")
    canvas.create_oval(60, 340, 190, 470, fill="white")
    canvas.update()
    time.sleep(1)
    
def redyellow():
    canvas.create_rectangle(50, 50, 200, 480, fill="grey")
    canvas.create_oval(60, 60, 190, 190, fill="red")
    canvas.create_oval(60, 200, 190, 330, fill="yellow")
    canvas.create_oval(60, 340, 190, 470, fill="white")
    canvas.update()
    time.sleep(1)
    
def green():
    canvas.create_rectangle(50, 50, 200, 480, fill="grey")
    canvas.create_oval(60, 60, 190, 190, fill="white")
    canvas.create_oval(60, 200, 190, 330, fill="white")
    canvas.create_oval(60, 340, 190, 470, fill="green")
    canvas.update()
    time.sleep(1)
    
def yellow():
    canvas.create_rectangle(50, 50, 200, 480, fill="grey")
    canvas.create_oval(60, 60, 190, 190, fill="white")
    canvas.create_oval(60, 200, 190, 330, fill="yellow")
    canvas.create_oval(60, 340, 190, 470, fill="white")
    canvas.update()
    time.sleep(1)

while True:
    red()
    redyellow()
    green()
    yellow()
    



