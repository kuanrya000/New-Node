from tkinter import*
import tkinter as tk
import tkinter.scrolledtext as tkst
import random
import time
import requests
import syllables
from aupyom import Sampler, Sound
from aupyom.util import GetSyllableAudio, example_audio_file

class MainScreen:
    def __init__(self, root):
        # The GUI
        self.root = root

        # Holds the audio of the string
        self.syllables_audio_list = []
        self.syllables_audio_list.append(syllables.Syllable())

        # An integer representing the place of the syllable we are working on in the syllables_audio-list
        self.syllable_pointer_number = 0

        # A list of all buttons showing the syllables at the top
        self.buttons_list = []

        # Audio player
        self.sampler = Sampler()

        # top frame that shows the syllables
        self.Tops = Frame(root, width=1100, height=200, bg="black", relief=SUNKEN)
        self.Tops.grid(row=0, column=0, columnspan=11, rowspan=2)
        self.Tops.grid_propagate(1)

        # text frame
        self.f1 = Frame(root, width=1100, height=403, bg="#333333", relief=SUNKEN)
        self.f1.grid(row=4, column=0, columnspan=11, rowspan=4)
        self.f1.grid_propagate(1)

        # right frame
        self.f2 = Frame(root, width=500, height=803, bg="#CAEBFF", relief=SUNKEN)
        self.f2.grid(row=0, column=11, columnspan=5, rowspan=8)
        self.f2.grid_propagate(1)

        # music
        self.f3 = Frame(root, width=1100, height=200, bg="#A9A9A9", relief=SUNKEN)
        self.f3.grid(row=2, column=0, columnspan=11, rowspan=2)
        self.f3.grid_propagate(1)


        self.vol_slider = Scale(self.f2, orient=HORIZONTAL, label='Volume', from_=-50, to=50, length=175, width=22, command=self.ChangeVol)

        self.pitch_slider = Scale(self.f2, orient=HORIZONTAL, label='Pitch', from_=-50, to=50, length=175, width=22, command=self.ChangePit)

        self.speed_slider = Scale(self.f2, orient=HORIZONTAL, label='Speed', from_=-50, to=50, length=175, width=22, command=self.ChangeSpd)

        self.vol_slider.pack()
        self.pitch_slider.pack()
        self.speed_slider.pack()



    def ChangeVol(self, val):
        self.syllables_audio_list[self.syllable_pointer_number].ChangeVolume(val)
    def ChangePit(self, val):
        self.syllables_audio_list[self.syllable_pointer_number].ChangePitch(val)
    def ChangeSpd(self, val):
        self.syllables_audio_list[self.syllable_pointer_number].ChangeLength(val)

    # Plays one sound
    def play_sound(self, num):
        if self.syllable_pointer_number != num:
            self.syllable_pointer_number = num
            self.SetSliderVal()
        self.sampler.play(self.syllables_audio_list[self.syllable_pointer_number].Activate())

    # Plays all sounds
    def play_sounds(self):
        start_time = time.time()
        for syllable in self.syllables_audio_list:
            while ((time.time() - start_time) <= syllable.start_time):
                pass
            self.sampler.play(syllable.Activate())

    # After clicking on a syllable button
    def SetSliderVal(self):
        self.vol_slider.set(self.syllables_audio_list[self.syllable_pointer_number].volume)
        self.speed_slider.set(self.syllables_audio_list[self.syllable_pointer_number].length)
        self.pitch_slider.set(self.syllables_audio_list[self.syllable_pointer_number].pitch)
        return

    def CreateButtons(self):
        x = 0
        for x in range(0, len(self.syllables_audio_list)):
            button = Button(self.Tops, bd=8, fg="black", font=('arial', 20, 'bold'), text = self.syllables_audio_list[x].audio_name,
                                            bg="powder blue", command=lambda num = x: self.play_sound(num), height = 0, width = 0)
            button.grid(row = 0, column = x)
            self.buttons_list.append(button)

    # Called when enter is hit
    def RemakeSyllables(self, string):
        for button in self.buttons_list:
            button.destroy()
        del self.buttons_list[:]
        syllables.SplitSyllables(self.syllables_audio_list, string)
        self.CreateButtons()

        if (self.syllables_audio_list):
            self.syllable_pointer = 0
            self.SetSliderVal()



def main():
    root = Tk()
    root.geometry("1600x800+0+0")
    root.state('zoomed')
    root.title("Vocaloid English")

    main_interface = MainScreen(root)

    # text box
    editArea = tkst.ScrolledText(
        master=main_interface.f1,
        wrap="word",
        width=int(135/2),
        height=int(24.5/2),
        bg="#FF0000",
        relief=SUNKEN
    )
    editArea.frame.pack(anchor='nw', fill="both", expand=1)
    editArea.pack(anchor='nw', fill="both", expand=1)
    editArea.configure(font=("Times New Roman", 24, "bold"))

    # Enter button
    enter_button = Button(main_interface.f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="Enter",
                               bg="powder blue", command=lambda: main_interface.RemakeSyllables(editArea.get("1.0", END)))
    enter_button.pack()

    play_button = Button(main_interface.f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="Play",
                              bg="powder blue", command=lambda: main_interface.play_sounds())
    play_button.pack()

    # audio = example_audio_file()
    # s1 = Sound.from_file(audio)
    # sampler.play(s1)
    # print(len(s1._sy) / s1.sr)



    # up_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Up", bg = "powder blue", command = lambda: s1.pitchchange(1)).grid(row = 2, column = 1)
    # down_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Down", bg = "powder blue", command = lambda: s1.pitchchange(-1)).grid(row = 2, column = 2)
    #
    # vup_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Up", bg = "powder blue", command = lambda: s1.volumechange(1)).grid(row = 3, column = 1)
    # vdown_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Down", bg = "powder blue", command = lambda: s1.volumechange(-1)).grid(row = 3, column = 2)
    #
    # sup_button = Button(Tops, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="Up", bg="powder blue", command=lambda: speedchanged(s1,.5)).grid(row=4, column=1)
    # sdown_button = Button(Tops, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="Down", bg="powder blue", command=lambda: speedchanged(s1,-.5)).grid(row=4, column=2)


    root.mainloop()

    return

if __name__ == "__main__":
    main()