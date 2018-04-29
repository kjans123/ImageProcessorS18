import os
from base64_conv_numpy import (encode_image_string, convert_image_to_np_array,
convert_processed_np_array_to_base64)
import numpy as np
import base64
import zipfile
import shutil


def b64_zip_to_b64_strings(b64_zip):
    """"Function that takes in a b64 encoded zip and outputs
       a list of b64 image strings

    :param b64_zip: b64 encoded zip string
    :raises ImportError: raises error when missing the following:
                         os, base64_conv_numpy, base64, zipfile
    :returns list_of_b64_strings: returns a list of b64 image strings
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
        import shutil
    except ImportError:
        msg = "Please make sure you have all packages."
        print(msg)
        logging.warning(msg)
    with open('decoded.zip', 'wb') as zf:
        bytes_b64_zip = b64_zip.encode('utf-8')
        zf.write(base64.b64decode(bytes_b64_zip))
        logging.info("File called decoded.zip was created.")
    zip_ref = zipfile.ZipFile('decoded.zip', 'r')
    path = 'Temporary/'
    if os.path.exists(path):
        logging.info("Check for path that exists")
        shutil.rmtree(path)
        logging.info("Remove directory")
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
                str_imgString = imgString.decode('utf-8')
                list_of_b64_strings.append(str_imgString)
    logging.info("Done traversing. Appended b64 encoded files \
                 that ended with .jpg or .JPG")
    shutil.rmtree('Temporary')
    logging.info("Remove directory Temporary")
    logging.info("Return the list of b64 strings")
    return list_of_b64_strings


def b64_strings_to_b64_zip(b64_strings, ext):
    """"Function that takes a list of base64 image strings and
       outputs a base64 zip of the images

    :param b64_strings: list of b64 processed image strings
    :param ext: string that describes what extension to use, e.g. : .png
    :raises ImportError: Error raised when the following modules
                         are not found: os, base64_conv_numpy,
                         checkListOfString, base64, zipfile, shutil
    :raises TypeError: Error raised if b64_strings is not a list of strings
    :returns b64_proc_zip_string: Returns b64 encoded zip string
    """
    import logging
    logging.basicConfig(filename="back_end.log",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    try:
        import os
        from base64_conv_numpy import (encode_image_string, convert_image_to_np_array,
        convert_processed_np_array_to_base64)
        from checkListOfString import check_list_of_string as check_list
        import base64
        import zipfile
        import shutil
    except ImportError:
        msg = "Please make sure you have all packages."
        print(msg)
        logging.warning(msg)
    path = 'imgs_directory/'
    if os.path.exists(path):
        logging.info("Check for path that exists")
        shutil.rmtree(path)
        logging.info("Remove directory")
    temp_folder = 'imgs_directory'
    os.mkdir(temp_folder)
    logging.info("Created temporary directory temp_folder to store images")
    if check_list(b64_strings):
        logging.info("Checked list of strings")
        for i, string in enumerate(b64_strings):
            image_out_name = 'image' + str(i) + ext
            # in a better version, we would pass in a list with original image name
            with open(os.path.join(temp_folder,image_out_name), 'wb') as img:
                # may need to add the os.path.sep in front of path name
                bytes_object = string.encode('utf-8')
                img.write(base64.b64decode(bytes_object))
        logging.info("Cycled through image strings to create images")
    else:
        msg = "Please provide a list of strings"
        logging.warning(msg)
        raise TypeError(msg)
    zfName = 'processed.zip'
    zipWrite = zipfile.ZipFile(zfName, 'w')
    for root, dirs, files in os.walk(temp_folder):
        for f in files:
            zipWrite.write(os.path.join(root,f))
    logging.info('processed.zip created')
    zipWrite.close()
    shutil.rmtree(temp_folder)
    logging.info('Temporary folder removed')
    b64_proc_zip = encode_image_string(zfName)
    logging.info("zip file base64 encoded")
    b64_proc_zip_string = b64_proc_zip.decode('utf-8')
    logging.info("Convert b64 bytes of zip to string")
    os.remove(zfName)
    logging.info("zip file deleted")
    return b64_proc_zip_string
