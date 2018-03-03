import urllib.request
import json
import re

# Split string base
SPLIT = ('\s|(?<!\d)[,.!?]')

# Takes the syllable in string form and finds the correct audio file based on it
class Syllable:
    length = 1
    pitch = 1
    audio = "SomeAudioFile"     # Not a string
    start_time = 0.0

    def __init__(self, audio_name):
        self.audio = audio_name
        return

    def Activate(self):
        #Run audio based on length and pitch
        return


# Takes a StringVar() and converts it into a list of words
def SplitInput(input_val):
    user_input = str(input_val.get())
    words_list = re.split(SPLIT, user_input)

    return words_list

# Takes a StringVar() and makes it into a list of syllables
def SplitSyllables(display_input):
    words_list = SplitInput(display_input)
    syllable_list = []

    for word in words_list:
        if word != "":
            word_syllables = Syllabize(word)
            if (word_syllables == None):
                print("%s could not be parsed.")
            else:
                for syllable in word_syllables:
                    syllable_list.append(syllable)

    for s in syllable_list:
        print(s)
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


