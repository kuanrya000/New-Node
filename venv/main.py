from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Vocaloid English")

Tops = Frame(root, width = 1600, height = 200, bg = "red", relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700, bg = "powder blue", relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root, width = 300, height = 700, bg = "powder blue", relief = SUNKEN)
f2.pack(side = RIGHT)

#added comment to test github

root.mainloop()