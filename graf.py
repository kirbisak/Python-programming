import random
import tkinter
canvas = tkinter.Canvas(width = 800, height = 500, bg="white")
canvas.pack()

def stupnica(n):
    znamky = [0, 0, 0, 0, 0]
    for i in range(n):
        j = random.randint(0, 4)
        znamky[j] += 1
    return znamky

def graf(func):
    canvas.create_line(50, 50, 50, 300)
    canvas.create_line(50, 300, 500, 300)
    k = 50
    for i in range(5):
        canvas.create_rectangle(60 + k - 40, 300, 60 + k, 300 - func[i]*20, fill="blue")
        k += 60

graf(stupnica(30))
