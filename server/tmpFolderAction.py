import json
import logging
import os
import shutil


def make_tmp(dictionary):
    """Makes a json file in a tmp folder to be downloaded after
       inputting a dictionary

    :param dictionary: dict object with post-processed image
                       in b64 string format
    :raises TypeError: error raised if input is not of type dict
    :raises ImportError: error raised if packages cannot be imported
    """
    logging.basicConfig(filename='back_end.log', format='%(asctime)s \
    %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info('Begin make_tmp')
    try:
        import json
        import os
        import shutil
    except ImportError:
        print("json, os, or shutil packages are not found!")
        logging.warning("json, os, or shutil packages are not found")
    # given json format data, create tmp folder
    try:
        jsonData = json.dumps(dictionary)
        logging.info('Create the json data from a dictionary')
    except TypeError:
        print("Please provide input in dictionary format!")
        logging.warning("Input needs to be of type dict")
    path = 'tmp/'
    if os.path.exists(path):
        logging.info('Check for path that exists')
        shutil.rmtree(path)
        logging.info('Remove directory')
    os.makedirs(path)
    logging.info('Create directory')
    with open('tmp/data.json', 'w') as outfile:
        logging.info('Write file called data.json in tmp folder')
        json.dump(jsonData, outfile)


def access_tmp():
    """Accesses tmp folder for the json and outputs a dictionary \
       to pass to front end

    :returns dict_object: returns a dictonary made from the JSON
                          file in temp/data.json. Dictionary
                          will subsquently be sent up to the
                          frontend for downloading
    :raises ImportError: error raised if json package not found
    :raises OSError: error raised if file path not accessible
    """
    logging.basicConfig(filename='back_end.log', format='%(asctime)s \
     %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info('Begin access_tmp')
    path = 'tmp/data.json'
    try:
        import json
    except ImportError:
        print("json package not found!")
        logging.warning("json package is not found!")
    with open(path, 'r') as infile:
        logging.info('Open json file in tmp folder')
        data = json.load(infile)
        logging.info('Read in data from json')
    logging.info('Create the dictionary from data string')
    dict_object = json.loads(data)
    logging.info('Return the dictionary')
    return dict_object
