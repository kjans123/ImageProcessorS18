from flask import Flask, jsonify, request
from flask_cors import CORS
from pymodm import connect
import datetime
from timeConvert import str2time, time2str
from checkListOfString import check_list_of_string
from check_for_user import Check_For_User

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
    """
    info = request.get_json()
    # Make sure the json received is correct
    try:
        email = info["user_email"]
    except KeyError:
        return jsonify("no email input"), 400
        print("No email input")
    check_email = Check_For_User(email)
    if check_email.user_exists is False:
        return jsonify(str(email) + " was not found. Please re-enter"), 400
        print(str(email) + " was not found. Please re-enter")
    try:
        pre_img = info["pre_b64_string"]
    except KeyError:
        return jsonify("no pre_image input"), 400
        print("Please provide pre_image base64 string")
    try:
        method = info["proc_method"]
    except KeyError:
        return jsonify("no proc_method input"), 400
        print("no processing method selected")

    try:
        isinstance(email, str)
        check_list_of_string(pre_img)
        isinstance(method, str)
    except TypeError:
        print("Please provide information in string format!")
    # if cases that will direct to the correct processing method
    # it would be better to import these methods from a separate file
    current_time = datetime.datetime.now()
    processed_list = []; # this is the list of strings of processed images
    for i, img in enumerate(pre_img):
        # for loop to go through all images
        # save user image with correct number
        # add method from main.py
        # save_image
        if method == "histeq":
            # Add function for histogram equalization
                # input is pre_img (depending on scikit or whatever,
                # may need to convert format then back to a b64 image string)
                # output is post_img
            #post_img = FOOBAR NOW, post_img should be list of strings
            # Once complete, save user action to database
                # remember we need to identify by __id or something
                # instead of adding with just email
                #add_hist from main.py
            # save processed b64 string
                # adds to the list of processed image strings in b64
            processed_list.append(post_img)
            if i == len(pre_img) - 1:  # last image in list
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img,
                    "post_b64_string": post_img, #last processed image
                    "action_time": time2str(duration),
                    "upload_time": time2str(current_time)
                }
                # need to add this list into some tmp folder
                # create_tmp function with json
                # input is (processed_list)
                return jsonify(new_info)
        elif method == "stretch":
            # Add function for contrast stretching
            # input is pre_img (depending on scikit or whatever,
                # may need to convert format then back to a b64 image string)
                # output is post_img
            #post_img = FOOBAR NOW, post_img should be list of strings
            # Once complete, save user action to database
                # remember we need to identify by __id or something
                # instead of adding with just email
                #add_hist from main.py
            # save processed b64 string
                # adds to the list of processed image strings in b64
            processed_list.append(post_img)
            if i == len(pre_img) - 1:  # last image in list
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img,
                    "post_b64_string": post_img, #last processed image
                    "action_time": time2str(duration),
                    "upload_time": time2str(current_time)
                }
                # need to add this list into some tmp folder
                # create_tmp function with json
                # input is (processed_list)
             
        elif method == "logcomp":
            # Add function for log compression
            # input is pre_img (depending on scikit or whatever,
                # may need to convert format then back to a b64 image string)
                # output is post_img
            #post_img = FOOBAR NOW, post_img should be list of strings
            # Once complete, save user action to database
                # remember we need to identify by __id or something
                # instead of adding with just email
                #add_hist from main.py
            # save processed b64 string
                # adds to the list of processed image strings in b64
            processed_list.append(post_img)
            if i == len(pre_img) - 1:  # last image in list
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img,
                    "post_b64_string": post_img, #last processed image
                    "action_time": time2str(duration),
                    "upload_time": time2str(current_time)
                }
                # need to add this list into some tmp folder
                # create_tmp function with json
                # input is (processed_list)
             
        elif method == "reverse":
            # Add function for reverse video
            # input is pre_img (depending on scikit or whatever,
                # may need to convert format then back to a b64 image string)
                # output is post_img
            #post_img = FOOBAR NOW, post_img should be list of strings
            # Once complete, save user action to database
                # remember we need to identify by __id or something
                # instead of adding with just email
                #add_hist from main.py
            # save processed b64 string
                # adds to the list of processed image strings in b64
            processed_list.append(post_img)
            if i == len(pre_img) - 1:  # last image in list
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img,
                    "post_b64_string": post_img, #last processed image
                    "action_time": time2str(duration),
                    "upload_time": time2str(current_time)
                }
                # need to add this list into some tmp folder
                # create_tmp function with json
                # input is (processed_list)


@app.route("/download", process=["GET"])
def download():
    # access tmp folder and output
