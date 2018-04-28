import os
from base64_conv_numpy import (encode_image_string, convert_image_to_np_array,
convert_processed_np_array_to_base64)
import numpy as np
import base64
import zipfile
## py file to be used for zip handling

# input b64 zip, decode, etc. on notebook
# output b64 list as would be given originally
# must only input jpg. actually could create temporary folder with those images and use glob command
# to just import all the jpg extension things (like with .csv)

def b64_zip_to_b64_strings(b64_zip):
    """Function that takes in a b64 encoded zip and outputs
       a list of b64 image strings

    :raises ImportError: raises error when missing the following:
                         os, base64_conv_numpy, base64, zipfile
    """
    import logging
    logging.basicConfig(filename="back_end.log",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    try:
        import os
        from base64_conv_numpy import (encode_image_string, convert_image_to_np_array,
        convert_processed_np_array_to_base64)
        import base64
        import zipfile
    except ImportError:
        msg = "Please make sure you have all packages."
        print(msg)
        logging.warning(msg)
    with open('decoded.zip', 'wb') as zf:
        zf.write(base64.b64decode(b64_zip))
        logging.info("File called decoded.zip was created.")
    zip_ref = zipfile.ZipFile('decoded.zip', 'r')
    os.mkdir('Temporary')
    logging.info("Create directory Temporary")
    zip_ref.extractall('Temporary')
    logging.info("Extract files from decoded.zip to Temporary")
    list_of_b64_strings = []
    logging.info("Traverse files with os.walk")
    for root, dirs, files in os.walk('Temporary'):
        for f in files:
            if f.endswith(('.jpg', '.JPG')):
                imgString = encode_image_string(os.path.join(root, f))
                list_of_b64_strings.append(imgString)
    logging.info("Done traversing. Appended b64 encoded files \
                 that ended with .jpg or .JPG")
    return list_of_b64_strings

def b64_strings_to_b64_zip(b64_strings):
    pass
