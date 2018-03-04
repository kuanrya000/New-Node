import urllib.request
import json

# Ideal case: inputs a string, returns lexical stress pronunciation list if it can, otherwise returns None
def Syllablize(input):

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
