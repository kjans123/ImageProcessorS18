import json
import logging
import os
import shutil

def make_tmp(dictionary):
    logging.basicConfig(filename='tmpFolderAction.log', mt='%(asctime)s \
    %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info('Begin make_tmp')
    #given json format data, create tmp folder
    jsonData = json.dumps(dictionary)
    logging.info('Create the json data from a dictionary')
    path = 'tmp/' #edit this path later!!!!!!!!
    if os.path.exists(path):
        logging.info('Check for path that exists')
        shutil.rmtree(path)
        logging.info('Remove directory')
    os.makedirs(path)
    logging.info('Create directory')
    with open('tmp/ .json', 'w') as outfile:
        json.dump(jsonData, outfile)

def access_tmp(path):
    logging.basicConfig(filename='tmpFolderAction.log', mt='%(asctime)s \
    %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info('Begin access_tmp')
    #given path, access tmp folder and output json data
    pass
