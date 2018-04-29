from zipHandler import (b64_strings_to_b64_zip as str2zip,
                        b64_zip_to_b64_strings as zip2str)
from base64_conv_numpy import encode_image_string as enco
import base64

def test_str2zip():
    imgString = enco("tiny.jpg")
    testList = [imgString.decode('utf-8')]
    b64_zip = str2zip(testList, ".jpg")
    b64_test_zip = enco("test_tiny3.zip")
    str_b64_test_zip = b64_test_zip.decode('utf-8')
    num_of_diff = 0.5*len([i for i in range(len(b64_zip)) if b64_zip[i] != str_b64_test_zip[i]])
    assert num_of_diff/len(b64_zip) < 0.01*len(b64_zip)

def test_zip2str():
    b64_str = zip2str("test_tiny3.zip")
    pass
