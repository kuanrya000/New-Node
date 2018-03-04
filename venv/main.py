from tkinter import*
import random
import time
import requests
import syllables
import pygame
import os
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


    #os.chdir("C:/Users/Ryan/Desktop/Github Folder/New-Node/venv/Lib/site-packages/aupyom/example_data/")
    sampler = Sampler()

    audio_file = example_audio_file()
    s1 = Sound.from_file(audio_file)
    sampler.play(s1)

    display_input = StringVar()

    Tops = Frame(root, width = 1600, height = 600, bg = "red", relief = SUNKEN)
    Tops.pack(side = TOP)

    # Gets text and puts it into display_input
    txtDisplay = Entry(Tops, font=('arial', 20, 'bold'), textvariable = display_input, bd = 30, insertwidth = 4, bg = "powder blue", justify = 'left')
    txtDisplay.grid(columnspan = 4)

    # Enter button
    enter_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Enter", bg = "powder blue", command = lambda: syllables.SplitSyllables(display_input)).grid(row = 2, column = 0)
    up_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Up", bg = "powder blue", command = lambda: s1.pitchchange(1)).grid(row = 2, column = 1)
    down_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Down", bg = "powder blue", command = lambda: s1.pitchchange(-1)).grid(row = 2, column = 2)

    vup_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Up", bg = "powder blue", command = lambda: s1.volumechange(1)).grid(row = 3, column = 1)
    vdown_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Down", bg = "powder blue", command = lambda: s1.volumechange(-1)).grid(row = 3, column = 2)

    sup_button = Button(Tops, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="Up", bg="powder blue", command=lambda: s1.speedchange(0.5)).grid(row=4, column=1)
    sdown_button = Button(Tops, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="Down", bg="powder blue", command=lambda: s1.speedchange(-0.5)).grid(row=4, column=2)

    root.mainloop()


    return

if __name__ == "__main__":
    main()