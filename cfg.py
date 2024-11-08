


### DANGER ZONE ###
import socket as s
def getkey():    
    return s.gethostname()

wraparound_hex = {
        "a": "0",
        "b": "1",
        "c": "2",
        "d": "3",
        "e": "4",
        "f": "5",
        "g": "6",
        "h": "7",
        "i": "8",
        "j": "9",
        "k": "a",
        "l": "b",
        "m": "c",
        "n": "d",
        "o": "e",
        "p": "f",        
        "q": "0",
        "r": "1",
        "s": "2",
        "t": "3",
        "u": "4",
        "v": "5",
        "w": "6",
        "x": "7",
        "y": "8",
        "z": "9",
        "-": "a"
    }

def wrap_hex(phrase):
    phrase = phrase.lower()
    new_phrase = phrase
    for i in phrase:
        if i in wraparound_hex:
            new_phrase = new_phrase.replace(i, wraparound_hex[i])
    return new_phrase

