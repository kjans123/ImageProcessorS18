from flask import Flask, jsonify, request
from flask_cors import CORS
from pymodm import connect
import datetime
from timeConvert import str2time, time2str
from checkListOfString import check_list_of_string

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
        check_list_of_string(pre_img)
        isinstance(method, str)
    except TypeError:
        print("Please provide information in string format!")
    # if cases that will direct to the correct processing method
    # it would be better to import these methods from a separate file
    current_time = datetime.datetime.now()
    if pre_img == "histeq":
        # Add function for histogram equalization
            # input is pre_img (depending on scikit or whatever,
            # may need to convert format then back to a b64 image string)
            # output is post_img
        #post_img = FOOBAR
        # Once complete, save user action to database
            # remember we need to identify by __id or something
            # instead of adding with just email
        new_info = {
            "user_email": email,
            "proc_method": method,
            "pre_b64_string": pre_img,
            "post_b64_string": post_img,
            "action_time": time2str(current_time)
        }
        return jsonify(new_info)
    elif pre_img == "stretch":
        # Add function for contrast stretching
        # Once complete, save user action to database
    elif pre_img == "logcomp":
        # Add function for log compression
        # Once complete, save user action to database
    elif pre_img == "reverse":
        # Add function for reverse video
        # Once complete, save user action to database


@app.route("/download", process=["GET"])
def download():
