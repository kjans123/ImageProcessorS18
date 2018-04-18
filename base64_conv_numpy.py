import base64
import numpy as np
import matplotlib
import PIL
from skimage import data
from skimage.util import img_as_ubyte
from skimage import io, exposure

def encode_image_string(filename):
    with open(filename, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string

def save_image_string(base64image, filename):
    s = base64.b64decode(base64image)
    sconv = np.frombuffer(s, dtype=np.uint8)
    sconv = img_as_ubyte(sconv)
    img_rescale = exposure.equalize_hist(sconv)
    image_s = base64.b64encode(img_rescale)
    image_s_d = base64.b64decode(image_s)
    with open(filename, "wb") as image_out:
        image_out.write(image_s_d)

if __name__ == '__main__':
    encoded_image = encode_image_string("haha.png")
    #print(encoded_image)
save_image_string(encoded_image, "haha2.png")
