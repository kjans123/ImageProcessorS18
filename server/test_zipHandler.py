from zipHandler import (b64_strings_to_b64_zip as str2zip,
                        b64_zip_to_b64_strings as zip2str)
from base64_conv_numpy import encode_image_string as enco
import os
import base64
import zipfile
import shutil


def test_str2zip():
    imgString = enco("tiny.jpg")
    testList = [imgString.decode('utf-8')]
    b64_zip = str2zip(testList, ".jpg")
    b64_test_zip = enco("test_tiny3.zip")
    str_b64_test_zip = b64_test_zip.decode('utf-8')
    num_of_diff = 0.5*len([i for i in range(len(b64_zip))
                           if b64_zip[i] != str_b64_test_zip[i]])
    assert num_of_diff/len(b64_zip) < 0.01*len(b64_zip)


def test_zip2str():
    zfName = "test_tiny3.zip"
    bytes_b64_zip = enco(zfName)
    str_b64_zip = bytes_b64_zip.decode('utf-8')
    b64_str = zip2str(str_b64_zip)
    zip_ref = zipfile.ZipFile(zfName)
    direc = 'Temp_test'
    os.mkdir(direc)
    str_list = []
    zip_ref.extractall(direc)
    for root, dirs, files in os.walk(direc):
        for f in files:
            imgString = enco(os.path.join(root, f))
            str_imgString = imgString.decode('utf-8')
            str_list.append(str_imgString)
    shutil.rmtree(direc)
    num_of_diff = 0.5*len([i for i in range(len(str_imgString[0]))
                           if str_imgString[0][i] != b64_str[0][i]])
    assert num_of_diff/len(b64_str[0]) < 0.01*len(b64_str[0])
