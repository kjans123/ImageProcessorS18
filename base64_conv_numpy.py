import base64
import numpy as np
import matplotlib
import PIL
from PIL import Image
from skimage import data
from skimage.util import img_as_ubyte
from skimage import io, exposure
import os

""""
"""
def encode_image_string(filename):
    with open(filename, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string


def convert_image_to_np_array(base64image):
    s = base64.b64decode(base64image)
    with open('temp.png', 'wb') as f:
        f.write(s)
        i = Image.open('temp.png')
        a = np.asarray(i)
    os.remove('temp.png')
    return a
