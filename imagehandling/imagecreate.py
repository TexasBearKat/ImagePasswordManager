import numpy as np
from PIL import Image

def create_image(name, height, width):
    pixels = np.random.randint(0, 255, (height, width, 3))
    pixels = np.array(pixels, dtype=np.uint8)
    image = Image.fromarray(pixels)
    image.save(f"{name}.png")

