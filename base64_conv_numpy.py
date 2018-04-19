import base64
import numpy as np
import PIL
from PIL import Image
import os

""""module that allows caller to convert a JPG image to base64 string,
    convert base64 string to numpy array and then convert the numpy
    array back to a base64 string

    :param filename: takes as input the file name of the JPG image
    :param base64image: takes as input the converted base64 image string
    :param npArray: takes as input the converted numpy image array
    :returns image_string: returns the image as base64 string
    :returns a: returns the base64 string converted to an image array
    :returns a_type: returns the datatype of the numpy array
    :returns m: returns the height dimension of the array
    :returns w: returns the width dimension of the array
    :returns z: returns the depth dimension of the array
    :returns img64: returns numpy array as base64 string
    :raises ValueError: will raise value error if incoming base64
                        string is empty
    :raises ValueError: wills raise value error if incoming numpy array
                        is empty
    :raises ImportError: raises error if package is not found in
                         virtual environment
"""


def encode_image_string(filename):
    """"function that encodes an image as base64 string

    :param filename: takes as input the file name of the JPG image
    :returns image_string: returns the image as base64 string
    :raises ImportError: raises error if package is not found in
                         virtual environment
    """
    import logging
    str1 = logging.DEBUG
    logging.basicConfig(filename="base64_conv_numpy.txt",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
    try:
        import base64
        with open(filename, "rb") as image_file:
            image_string = base64.b64encode(image_file.read())
            logging.info("success: converted image to base64")
            return image_string
    except ImportError:
        print("base64 package not found")
        logging.warning("base64 package not found")


def convert_image_to_np_array(base64image):
    """"function that converts base64 to temporary JPG then
        to a numpy array

    :param base64image: takes as input the converted base64 image string
    :returns a: returns the base64 string converted to an image array
    :returns a_type: returns the datatype of the numpy array
    :returns m: returns the height dimension of the array
    :returns w: returns the width dimension of the array
    :returns z: returns the depth dimension of the array
    :raises ValueError: will raise value error if incoming base64
                        string is empty
    :raises ImportError: raises error if package is not found in
                         virtual environment
    """
    import logging
    str1 = logging.DEBUG
    logging.basicConfig(filename="base64_conv_numpy.txt",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
    try:
        import base64
        import numpy as np
        import PIL
        from PIL import Image
        import os
        if base64image is None or base64image == [] or base64image == "":
            logging.warning("base64 image string is EMPTY")
            raise ValueError("empty base64 string")
        s = base64.b64decode(base64image)
        with open('temp.JPG', 'wb') as f:
            f.write(s)
            i = Image.open('temp.JPG')
            a = np.asarray(i)
        os.remove('temp.JPG')
        a_type = a.dtype
        shape_tuple = a.shape
        m = shape_tuple[0]
        w = shape_tuple[1]
        z = shape_tuple[2]
        logging.info("success: base64 image converted to np array")
        return a, a_type, m, w, z
    except ImportError:
        print("base64/numpy/PIL/os packages not found. Check virtualenv")
        msg = 'base64/numpy/PIL/os packages not found. Check virtualenv'
        logging.warning(msg)


def convert_processed_np_array_to_base64(npArray):
    """"function that converts numpy array to a a temporary JPG
        then to a base64 string

    :param npArray: takes as input the converted numpy image array
    :returns img64: returns numpy array as base64 string
    :raises ValueError: wills raise value error if incoming numpy array
                        is empty
    :raises ImportError: raises error if package is not found in
                         virtual environment
    """
    import logging
    str1 = logging.DEBUG
    logging.basicConfig(filename="base64_conv_numpy.txt",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
    try:
        import base64
        import numpy as np
        import PIL
        from PIL import Image
        import os
        h = np.array([])
        if (npArray is None or npArray.all() == [] or npArray == "" or
                npArray.all() == h):
            logging.warning("numpy array is EMPTY")
            raise ValueError("empty numpy array")
        img = Image.fromarray(npArray)
        img.save('temp.JPG')
        img64 = encode_image_string('temp.JPG')
        os.remove('temp.JPG')
        logging.info("success: numpy array converted to base64 string")
        return img64
    except ImportError:
        print("base64/numpy/PIL/os packages not found. Check virtualenv")
        msg = 'base64/numpy/PIL/os packages not found. Check virtualenv'
        logging.warning(msg)
