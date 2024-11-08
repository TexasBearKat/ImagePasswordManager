import numpy as np
from PIL import Image

from os import path
import sys
sys.path.append(path.abspath("../ImagePasswordManager"))
import cfg

key = cfg.getkey().lower()
wraparound_hex = cfg.wrap_hex_dict()

def wrap_hex(phrase):
    new_phrase = phrase
    for i in phrase:
        if i in wraparound_hex:
            new_phrase = new_phrase.replace(i, wraparound_hex[i])
    return new_phrase

def decode(name, image_type):
    Image.MAX_IMAGE_PIXELS = None 

    bad_characters = ['[', ']', '.', ' ', '\n']

    img_array = np.asarray(Image.open(f"{name}.{image_type}"))
    string_array = np.array_str(img_array)
    final_string = ""
    for item in string_array:
        for item2 in item:
            if item2 in bad_characters:
                continue
            final_string += item2
    
    hex_final_string = hex(int(final_string))
    return hex_final_string[2:]
