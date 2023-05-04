import random
import tkinter
import time
canvas = tkinter.Canvas(width=800, height=500, bg="white")
canvas.pack()

def farba():
    color = "#"
    for i in range(3):
        f = random.randint(0,255)
        color += format(f, "02x")
    return color

print(farba())


def balony(n):
    for i in range(n):
        x = random.randint(1, 800)
        y = random.randint(1, 500)
        r = random.randint(1, 50)
        canvas.create_oval(x, y, x+r, y+r, fill=farba())
        time.sleep(0.1)
        canvas.update()

balony(100)

