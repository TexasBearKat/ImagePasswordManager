import numpy as np
from PIL import Image


def create_image(name, image_type, height, width):

    pixels = np.random.randint(0, 255, (height, width, 3))
    pixels = np.array(pixels, dtype=np.uint8)

    image = Image.fromarray(pixels)
    image.save(f"{name}.{image_type}")

create_image("test_image2", "png", 8000, 8000)
