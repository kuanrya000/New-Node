from tkinter import*
import random
import time
import requests
import syllables

#json_stuff = 'http://api.datamuse.com/words?sp=example&d=sp&md=fr&max=1' | python -mjson.tool

def main():
    root = Tk()
    root.geometry("1600x800+0+0")
    root.state('zoomed')
    root.title("Vocaloid English")

    display_input = StringVar()

    Tops = Frame(root, width = 1600, height = 600, bg = "red", relief = SUNKEN)
    Tops.pack(side = TOP)

    # Gets text and puts it into display_input
    txtDisplay = Entry(Tops, font=('arial', 20, 'bold'), textvariable = display_input, bd = 30, insertwidth = 4, bg = "powder blue", justify = 'left')
    txtDisplay.grid(columnspan = 4)

    # Enter button
    enter_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Enter", bg = "powder blue", command = lambda: syllables.SplitSyllables(display_input)).grid(row = 2, column = 0)

    root.mainloop()
    return

main()