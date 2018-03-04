import urllib.request
import json
import re
from aupyom import Sampler, Sound
from aupyom.util import example_audio_file, GetSyllableAudio

# Split string base
SPLIT = ('\s|(?<!\d)[,.!?]')

# Takes the syllable in string form and finds the correct audio file based on it
class Syllable:

    def __init__(self, name = ""):
        self.length = 0
        self.pitch = 0
        self.volume = 0
        self.start_time = 0.0
        self.audio_name = name

        if self.audio_name != "":
            self.audio = GetSyllableAudio(self.audio_name)
        else:
            self.audio = example_audio_file()

        self.sound = Sound.from_file(self.audio)
        self.duration = len(self.sound.y) / self.sound.sr

        return


    def ChangePitch(self, num):
        self.pitch = float(num)
        self.sound.pitchchange(self.pitch)

    def ChangeLength(self, num):
        self.length = float(num)
        self.sound.speedchange(self.length)
        self.duration = len(self.sound.y)/(self.sound.stretch_factor)

    def ChangeVolume(self, num):
        self.volume = float(num)
        self.sound.volumechange(self.volume)

    def ChangeStartTime(self, num):
        self.start_time = float(num)

    def Activate(self):
        return self.sound


# Takes a StringVar() and converts it into a list of words
def SplitInput(input_val):
    #user_input = str(input_val.get())
    words_list = re.split(SPLIT, input_val)

    return words_list

# Takes a StringVar() and makes it into a list of syllables
def SplitSyllables(audio_list, display_input):
    words_list = SplitInput(display_input)
    syllable_list = []
    del audio_list[:]

    if len(words_list) == 0:
        audio_list = []
        return

    for word in words_list:
        if word != "":
            word_syllables = Syllabize(word)
            if (word_syllables == None):
                print("%s could not be parsed." %word)
            else:
                for syllable in word_syllables:
                    syllable_list.append(syllable)

    for s in syllable_list:
        temp = Syllable(s)
        audio_list.append(temp)

    for x in range(1, len(audio_list)):
        audio_list[x].start_time = audio_list[x - 1].duration + audio_list[x - 1].start_time

    return

# Ideal case: inputs a string, returns lexical stress pronunciation list if it can, otherwise returns None
def Syllabize(input):
    # Attempt to fetch url for API
    try:
        url = "http://api.datamuse.com/words?sp=" + input + "&d=sp&md=fr&max=1"
    except NameError:
        return None

    # Parse url
    object = urllib.request.urlopen(url).read()
    data = json.loads(object)

    # Attempt to grab pronunciation data (from a list)
    try:
        output = data[0]['tags'][0][5:].split(" ")
    except IndexError:
        return None
    output = output[:-1]

    return output


