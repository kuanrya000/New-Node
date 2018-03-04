from tkinter import*
import tkinter as tk
import tkinter.scrolledtext as tkst
import random
import time
import requests
import syllables
from aupyom import Sampler, Sound
from aupyom.util import example_audio_file

#json_stuff = 'http://api.datamuse.com/words?sp=example&d=sp&md=fr&max=1' | python -mjson.tool

def pitchchange(sound, num):
    sound.pitch_shift += num
    return

def main():
    root = Tk()
    root.geometry("1600x800+0+0")
    root.state('zoomed')
    root.title("Vocaloid English")

    sampler = Sampler()
    display_input = StringVar()
    syllables_audio_list = []

    # top frame that shows the syllables
    Tops = Frame(root, width=1100, height=200, bg="black", relief=SUNKEN)
    Tops.grid(row=0, column=0, columnspan = 11, rowspan = 2)

    # right frame
    f2 = Frame(root, width=500, height=803, bg="#CAEBFF", relief=SUNKEN)
    f2.grid(row=0, column=11, columnspan = 5, rowspan = 8)

    # music
    f3 = Frame(root, width=1100, height=200, bg="#A9A9A9", relief=SUNKEN)
    f3.grid(row=2, column=0, columnspan = 11, rowspan = 2)

    f1 = Frame(root, width=1100, height=403, bg="#333333", relief=SUNKEN)
    f1.grid(row=4, column=0, columnspan=11, rowspan = 4)
    #text box
    editArea = tkst.ScrolledText(
        master=f1,
        wrap="word",
        width=135,
        height=24.5,
        bg = "#FF0000",
        relief=SUNKEN
    )
    editArea.frame.pack(anchor='nw', fill="both", expand=1)
    editArea.pack(anchor='nw', fill="both", expand=1)

    # Gets text and puts it into display_input
    txtDisplay = Entry(Tops, font=('arial', 20, 'bold'), textvariable = display_input, bd = 30, insertwidth = 4, bg = "powder blue", justify = 'left')
    txtDisplay.grid(columnspan = 4)

    # Enter button
    enter_button = Button(f2, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Enter", bg = "powder blue", command = lambda: syllables.SplitSyllables(syllables_audio_list, display_input)).grid(row = 2, column = 0)

    # up_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Up", bg = "powder blue", command = lambda: s1.pitchchange(1)).grid(row = 2, column = 1)
    # down_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Down", bg = "powder blue", command = lambda: s1.pitchchange(-1)).grid(row = 2, column = 2)
    #
    # vup_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Up", bg = "powder blue", command = lambda: s1.volumechange(1)).grid(row = 3, column = 1)
    # vdown_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Down", bg = "powder blue", command = lambda: s1.volumechange(-1)).grid(row = 3, column = 2)
    #
    # sup_button = Button(Tops, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="Up", bg="powder blue", command=lambda: s1.speedchange(0.5)).grid(row=4, column=1)
    # sdown_button = Button(Tops, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="Down", bg="powder blue", command=lambda: s1.speedchange(-0.5)).grid(row=4, column=2)

    root.mainloop()

    return

if __name__ == "__main__":
    main()