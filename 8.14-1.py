#nandelbrot set
from tkinter import *
def mandel(c):
    z=0
    for i in range(30):
        z=z**2+c
        if abs(z)>2: break
    return abs(z) < 2

#driver code
root = Tk()
size=800
w = Canvas(root, width=size,height=size)
w.pack()
print('Now drawing....')
for x in range(size):
    for y in range(size):
        real,img = x/size*4-2, 2-y/size*4
        c = complex(real, img)
        if mandel(c):
            w.create_line(x,y,x+1,y+1,fill="black")
root.mainloop()