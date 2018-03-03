from tkinter import*
import random
import time
import requests

#json_stuff = 'http://api.datamuse.com/words?sp=example&d=sp&md=fr&max=1' | python -mjson.tool

# Split string base
SPLIT = ("; |,.!?")

# Takes the syllable in string form and finds the correct audio file based on it
class Syllable:
    length = 1
    pitch = 1
    audio = "SomeAudioFile"     # Not a string
    start_time = 0.0

    def __init__(self, audio_name):
        self.audio = audio_name
        return

<<<<<<< HEAD
    def Activate(self):
        #Run audio based on length and pitch
        return

=======
#added comment to test github
>>>>>>> ef8a1d065796ebe26ee00351da665ae6780fa95a

# Takes a StringVar() and converts it into a list of words
def SplitInput(input_val):
    user_input = str(input_val.get())
    words_list = user_input.split(SPLIT)
    return words_list

def GetWordsList(display_input):
    words_list = SplitInput(display_input)
    print(words_list)
    return

def main():
    root = Tk()
    root.geometry("1600x800+0+0")
    root.state('zoomed')
    root.title("Vocaloid English")

    display_input = StringVar()

    Tops = Frame(root, width = 1600, height = 600, bg = "red", relief = SUNKEN)
    Tops.pack(side = TOP)

    txtDisplay = Entry(Tops, font=('arial', 20, 'bold'), textvariable = display_input, bd = 30, insertwidth = 4, bg = "powder blue", justify = 'left')
    txtDisplay.grid(columnspan = 4)

    enter_button = Button(Tops, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'), text = "Enter", bg = "powder blue", command = lambda: GetWordsList(display_input)).grid(row = 2, column = 0)

    root.mainloop()
    return

main()