import numpy as np

from matplotlib import pyplot as plt


from skimage.util import img_as_ubyte
from skimage import exposure

import base64
from PIL import Image





# Load an example image

imgo = Image.open('haha.png')
data = np.array(imgo, dtype=np.uint8)
img = img_as_ubyte(data)

# Global equalize
img_rescale = exposure.equalize_hist(img)

# Equalization
#selem = disk(30)
#img_eq = rank.equalize(img, selem=selem)


plt.imshow(img_rescale)
plt.show()
