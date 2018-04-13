from flask import Flask, jsonify, request
from flask_cors import CORS
from pymodm import connect
import datetime

app = Flask(__name__)
CORS(app)
connect("mongodb://vcm-3594.vm.duke.edu:27017/image_process_app")

@app.route("/", methods=["GET"])
def welcome():
    """ Function that greets the user on the main page!
    """
    return "Welcome to CrunchWrap Pizza Image Processor!"

@app.route("/process", methods=["POST"])
def process():
    """Function that processes the pre-processed image.
    
    :raises ValueError: Error raised for incorrect json format
    :raises TypeError: Error raised if values provided are incorrect type
    """
    info = request.get_json()
    # Make sure the json received is correct
    try:
        email = info["user_email"]
        pre_img = info["pre_b64_string"]
        method = info["proc_method"]
    except ValueError:
        print("Please provide the correct json format!")

    try:
        isinstance(email, str)
        isinstance(pre_img, str)
        isinstance(method, str)
    except TypeError:
        print("Please provide information in string format!")
    # if cases that will direct to the correct processing method
    # it would be better to import these methods from a separate file
    if pre_img == "histeq":
        # Add function for histogram equalization
    elif pre_img == "stretch":
        # Add function for contrast stretching
    elif pre_img == "logcomp":
        # Add function for log compression
    elif pre_img == "reverse":
        # Add function for reverse video
    else:
        print("How the heck did you get here? The dropdown should have inputted the correct
              string.")

    # return json as specified in google doc


