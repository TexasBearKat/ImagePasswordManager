import numpy as np
from PIL import Image
import cfg

key = cfg.getkey()
wraparound_hex = cfg.wrap_hex_dict()

def wrap_hex(phrase):
    new_phrase = phrase
    for i in phrase:
        if i in wraparound_hex:
            new_phrase.replace(i, wraparound_hex[i])
    return new_phrase

def decode(name, image_type):
    Image.MAX_IMAGE_PIXELS = None 

    img = Image.open(f"{name}.{image_type}")
    img_array = np.asarray(img)
    
    total = np.sum(img_array, dtype=np.uint64)
    total = total ** 3 + total * int(wrap_hex(key), 16)
    total_h = hex(int(total))
    print(total_h[2:])

decode("test_image", "png")

