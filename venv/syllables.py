import urllib.request
import json
import re
from aupyom import Sampler, Sound
from aupyom.util import GetSyllableAudio

# Split string base
SPLIT = ('\s|(?<!\d)[,.!?]')

# Takes the syllable in string form and finds the correct audio file based on it
class Syllable:

    def __init__(self, audio_name):
        self.length = 1
        self.pitch = 1
        self.volume = 1
        self.start_time = 0.0
        self.audio = GetSyllableAudio(audio_name)
        self.sound = Sound.from_file(self.audio)
        return

    def ChangePitch(self, num):
        self.pitch = num
        self.sound.pitchchange(self.pitch)

    def ChangeLength(self, num):
        self.length = num
        self.sound.speedchange(self.length)

    def ChangeVolume(self, num):
        self.volume = num
        self.sound.volumechange(self.volume)

    def ChangeStartTime(self, num):
        self.start_time = num

    def Activate(self):
        return self.sound


# Takes a StringVar() and converts it into a list of words
def SplitInput(input_val):
    user_input = str(input_val.get())
    words_list = re.split(SPLIT, user_input)

    return words_list

# Takes a StringVar() and makes it into a list of syllables
def SplitSyllables(audio_list, display_input):
    words_list = SplitInput(display_input)
    syllable_list = []

    if len(words_list) == 0:
        audio_list = []
        return

    for word in words_list:
        if word != "":
            word_syllables = Syllabize(word)
            if (word_syllables == None):
                print("%s could not be parsed.")
            else:
                for syllable in word_syllables:
                    syllable_list.append(syllable)

    for s in syllable_list:
        temp = Syllable(s)
        audio_list.append(temp)

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


