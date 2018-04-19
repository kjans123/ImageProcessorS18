import json
import logging
import os
import shutil

def make_tmp(dictionary):
    """Makes a json file in a tmp folder

    :param dictionary: dict object with post-processed image in b64 string format
    """
    #logging.basicConfig(filename='tmpFolderAction.log', mt='%(asctime)s \
    #%(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info('Begin make_tmp')
    #given json format data, create tmp folder
    jsonData = json.dumps(dictionary)
    logging.info('Create the json data from a dictionary')
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
    #logging.basicConfig(filename='tmpFolderAction.log', mt='%(asctime)s \
    #%(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info('Begin access_tmp')
    # access tmp folder and output json data
    path = 'tmp/data.json'
    # if not checked in front end, move below into try/except
    # to check for that the tmp folder exists
    with open(path, 'r') as infile:
        logging.info('Open json file in tmp folder')
        data = json.load(infile)
        logging.info('Read in data from json')
    # this creates a string! We need to convert this string
    # into the dictionary
    dict_object = json.loads(data)
    return dict_object
