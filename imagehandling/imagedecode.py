import numpy as np
from PIL import Image


def decode(name, image_type):
    img = Image.open(f"{name}.{image_type}")
    img_array = np.asarray(img)

    total = 0
    print(np.sum(img_array, dtype=np.uint64))

decode("test_image", "png")

