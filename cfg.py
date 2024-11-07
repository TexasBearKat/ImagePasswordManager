import socket as s

def getkey():
    return s.gethostname()

def wrap_hex_dict():
    return {
        "q": "1",
        "r": "2",
        "s": "3",
        "t": "4",
        "u": "5",
        "v": "6",
        "w": "7",
        "x": "8",
        "y": "9",
        "z": "a",
        "-": "b"
    }