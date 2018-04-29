from flask import Flask, jsonify, request
from flask_cors import CORS
from pymodm import connect
import datetime
from timeConvert import str2time, time2str
from checkListOfString import check_list_of_string
from check_for_user import Check_For_User
from tmpFolderAction import make_tmp, access_tmp
from base64_conv_numpy import encode_image_string
from base64_conv_numpy import convert_image_to_np_array
from base64_conv_numpy import convert_processed_np_array_to_base64
from zipHandler import (b64_zip_to_b64_strings,
                        b64_strings_to_b64_zip)
from histo_equal import histo_equal
from logCompression import logComp
from reverseVideo import reverseVid
from contr_strech import contr_stretch
from create_histo import create_histo
from main import create_user
from main import (add_log, add_contr, add_histo, add_rever)
from main import save_image
from zipHandler import (b64_strings_to_b64_zip, b64_zip_to_b64_strings)
import glob
import logging
import os

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

    :returns: json with information to display pre- and post- \
            processed images
    """
    logging.basicConfig(filename='back_end.log', format='%(asctime)s \
    %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info("Begin app route to /process")
    info = request.get_json()
    try:
        email = info["user_email"]
    except KeyError:
        print("No email input")
        return jsonify("no email input"), 400
    check_email = Check_For_User(email)
    if check_email.user_exists is False:
        cu = create_user(email)
        print(str(email) + " was not found. User created")
    try:
        pre_img = info["pre_b64_string"]
    except KeyError:
        print("Please provide pre_image base64 string")
        return jsonify("no pre_image input"), 400
    try:
        method = info["proc_method"]
    except KeyError:
        print("no processing method selected")
        return jsonify("no proc_method input"), 400
    try:
        isinstance(email, str)
        check_list_of_string(pre_img)
        isinstance(method, str)
    except TypeError:
        print("Please provide information in string format!")
        return jsonify("email is not string"), 400
    jpgList = glob.glob("/images"+str(email)+"/.*")
    jpgCount = len(jpgList)
    print(jpgCount)
    current_time = datetime.datetime.now()
    processed_list = []
    processed_histograms = []
    pre_img_list = []
    pre_img_histograms = []
    jpgFileNum = jpgCount
    for i, img in enumerate(pre_img):
        if method == "Histogram Equalization":
            if jpgFileNum == 0:
                os.makedirs(('/images/'+str(email)))
            jpgFileNum = jpgFileNum + 1
            filename = '/images/'+str(email)+'/'+str(jpgFileNum)+'.jpg'
            with open(filename, "wb") as image_out:
                image_out.write(base64.b64decode(img))
            iSave = save_image(email, jpgFileNum)
            iHisto = add_histo(email)
            imgArray, a_type, m, w, z = convert_image_to_np_array(img)
            hist_image = histo_equal(imgArray)
            histogram_of_pre_img = create_histo(imgArray)
            histogram_of_post_img = create_histo(hist_equal_image)
            hist_img64 = convert_processed_np_array_to_base64(hist_image)
            processed_list.append(hist_img64)
            pre_img_list.append(pre_img)
            processed_histograms.append(histogram_of_post_img)
            pre_img_histograms.append(histogram_of_pre_img)
            return_size = (str(m)+str(w) + ' pixels')
            if i == len(pre_img) - 1:
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": time2str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size
                }
                make_tmp(new_info)
                return jsonify(new_info)
        elif method == "Contrast Stretching":
            jpgFileNum = jpgFileNum + 1
            filename = '/images/'+str(email)+'/'+str(jpgFileNum)+'.jpg'
            with open(filename, "wb") as image_out:
                image_out.write(base64.b64decode(img))
            iSave = save_image(email, jpgFileNum)
            iContr = add_contr(email)
            imgArray, a_type, m, w, z = convert_image_to_np_array(img)
            hist_image = contr_stretch(imgArray)
            histogram_of_pre_img = create_histo(imgArray)
            histogram_of_post_img = create_histo(hist_equal_image)
            hist_img64 = convert_processed_np_array_to_base64(hist_image)
            processed_list.append(hist_img64)
            pre_img_list.append(pre_img)
            processed_histograms.append(histogram_of_post_img)
            pre_img_histograms.append(histogram_of_pre_img)
            return_size = (str(m)+str(w) + ' pixels')
            return_size = (str(m)+str(w) + ' pixels')
            if i == len(pre_img) - 1:
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": time2str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size
                }
                make_tmp(new_info)
                return jsonify(new_info)
        elif method == "Log Compression":
            jpgFileNum = jpgFileNum + 1
            filename = '/images/'+str(email)+'/'+str(jpgFileNum)+'.jpg'
            with open(filename, "wb") as image_out:
                image_out.write(base64.b64decode(img))
            iSave = save_image(email, jpgFileNum)
            iLog = add_log(email)
            imgArray, a_type, m, w, z = convert_image_to_np_array(img)
            hist_image = logComp(imgArray)
            histogram_of_pre_img = create_histo(imgArray)
            histogram_of_post_img = create_histo(hist_equal_image)
            hist_img64 = convert_processed_np_array_to_base64(hist_image)
            processed_list.append(hist_img64)
            pre_img_list.append(pre_img)
            processed_histograms.append(histogram_of_post_img)
            pre_img_histograms.append(histogram_of_pre_img)
            return_size = (str(m)+str(w) + ' pixels')
            if i == len(pre_img) - 1:
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": time2str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size
                }
                make_tmp(new_info)
                return jsonify(new_info)
        elif method == "Reverse Video":
            jpgFileNum = jpgFileNum + 1
            filename = '/images/'+str(email)+'/'+str(jpgFileNum)+'.jpg'
            with open(filename, "wb") as image_out:
                image_out.write(base64.b64decode(img))
            iSave = save_image(email, jpgFileNum)
            iRev = add_rever(email)
            imgArray, a_type, m, w, z = convert_image_to_np_array(img)
            hist_image = reverseVid(imgArray)
            histogram_of_pre_img = create_histo(imgArray)
            histogram_of_post_img = create_histo(hist_equal_image)
            hist_img64 = convert_processed_np_array_to_base64(hist_image)
            processed_list.append(hist_img64)
            pre_img_list.append(pre_img)
            processed_histograms.append(histogram_of_post_img)
            pre_img_histograms.append(histogram_of_pre_img)
            return_size = (str(m)+str(w) + ' pixels')
            if i == len(pre_img) - 1:
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                logging.info("Create json to be sent to frontend for preview")
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": time2str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size
                }
                make_tmp(new_info)
                return jsonify(new_info)


@app.route("/download", methods=["GET"])
def download():
    # access tmp folder and output
    output = access_tmp()
    return jsonify(output)
