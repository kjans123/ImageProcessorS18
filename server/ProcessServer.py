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
from giveMeHeader import getHeader
import glob
import logging
import os
import base64
import stat

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
    info = request.json
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
        extension = info["file_type"]
    except KeyError:
        print("Please provide file_type")
        return jsonify("no file type provided"), 400
    try:
        header = info["header"]
    except KeyError:
        print("no header string")
        return jsonify("no header string"), 400
    if extension == 'JPEG':
        extension = '.jpg'
    elif extension == 'PNG':
        extension == '.png'
    elif extension == 'TIFF':
        extension == '.tif'
    else:
        raise ValueError("Did not select an appropriate extension!")
    try:
        isinstance(email, str)
        #check_list_of_string(pre_img)
        #nolonger list of string (yes this screw pep8 on purpose)
        isinstance(method, str)
    except TypeError:
        print("Please provide information in string format!")
        return jsonify("email is not string"), 400
    jpgList = glob.glob("images/"+str(email)+"/*")
    jpgCount = len(jpgList)
    print(jpgCount)
    current_time = datetime.datetime.now()
    processed_list = []
    processed_histograms = []
    pre_img_list = []
    pre_img_histograms = []
    jpgFileNum = jpgCount
    if 'zip' in header:
        pre_img = b64_zip_to_b64_strings(pre_img)
        pass
    elif 'jpeg' in header:
        pass
    else:
        raise ValueError("Input is not a b64 zip or jpg list!")
    for i in range(len(pre_img)):
        img = pre_img[i]
        print(img[0:100])
        if method == "Histogram Equalization":
            if jpgFileNum == 0:
                os.chmod('images',stat.S_IRWXU)
                os.makedirs(('images/'+str(email)))
                os.chmod(('images/'+str(email)),stat.S_IRWXU)
            jpgFileNum = jpgFileNum + 1
            filename = 'images/'+str(email)+'/'+str(jpgFileNum)+'.jpg'
            with open(filename, "wb") as image_out:
                image_out.write(base64.b64decode(img))
            iSave = save_image(email, jpgFileNum)
            iHisto = add_histo(email)
            imgArray, a_type, m, w, z = convert_image_to_np_array(img)
            hist_image = histo_equal(img)
            histogram_of_pre_img = create_histo(imgArray)
            histogram_of_post_img = create_histo(hist_image)
            hist_img64 = convert_processed_np_array_to_base64(hist_image)
            processed_list.append(getHeader(extension) + str(hist_img64))
            pre_img_list.append(getHeader(extension) + img)
            processed_histograms.append(getHeader() + str(histogram_of_post_img))
            pre_img_histograms.append(getHeader() + str(histogram_of_pre_img))
            return_size = (str(m)+str(w) + ' pixels')
            if i == len(pre_img) - 1 and i > 0:
                # we need to zip
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                zipped_list = b64_strings_to_b64_zip(processed_list, extension)
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size,
                    "b64_zip_out": getHeader(".zip") + zipped_list
                }
                make_tmp(new_info)
                return jsonify(new_info),200
            elif i == len(pre_img) - 1 and i == 0:
                # we don't need to zip. single image
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size
                }
                make_tmp(new_info)
                return jsonify(new_info),200
        elif method == "Contrast Stretching":
            if jpgFileNum == 0:
                os.chmod('images',stat.S_IRWXU)
                os.makedirs(('images/'+str(email)))
                os.chmod(('images/'+str(email)),stat.S_IRWXU)
            jpgFileNum = jpgFileNum + 1
            filename = 'images/'+str(email)+'/'+str(jpgFileNum)+'.jpg'
            with open(filename, "wb") as image_out:
                image_out.write(base64.b64decode(img))
            iSave = save_image(email, jpgFileNum)
            iContr = add_contr(email)
            imgArray, a_type, m, w, z = convert_image_to_np_array(img)
            hist_image = contr_stretch(img)
            histogram_of_pre_img = create_histo(imgArray)
            histogram_of_post_img = create_histo(hist_image)
            hist_img64 = convert_processed_np_array_to_base64(hist_image)
            processed_list.append(getHeader(extension) + str(hist_img64))
            pre_img_list.append(getHeader(extension) + img)
            processed_histograms.append(getHeader() + str(histogram_of_post_img))
            pre_img_histograms.append(getHeader() + str(histogram_of_pre_img))
            return_size = (str(m)+str(w) + ' pixels')
            return_size = (str(m)+str(w) + ' pixels')
            if i == len(pre_img) - 1 and i > 0:
                # we need to zip
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                zipped_list = b64_strings_to_b64_zip(processed_list, extension)
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size,
                    "b64_zip_out": getHeader(".zip") + zipped_list
                }
                make_tmp(new_info)
                return jsonify(new_info),200
            elif i == len(pre_img) - 1 and i == 0:
                # we don't need to zip. single image
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size
                }
                make_tmp(new_info)
                return jsonify(new_info),200
        elif method == "Log Compression":
            if jpgFileNum == 0:
                os.chmod('images',stat.S_IRWXU)
                os.makedirs(('images/'+str(email)))
                os.chmod(('images/'+str(email)),stat.S_IRWXU)
            jpgFileNum = jpgFileNum + 1
            filename = 'images/'+str(email)+'/'+str(jpgFileNum)+'.jpg'
            with open(filename, "wb") as image_out:
                image_out.write(base64.b64decode(img))
            iSave = save_image(email, jpgFileNum)
            iLog = add_log(email)
            imgArray, a_type, m, w, z = convert_image_to_np_array(img)
            hist_image = logComp(img)
            histogram_of_pre_img = create_histo(imgArray)
            histogram_of_post_img = create_histo(hist_image)
            hist_img64 = convert_processed_np_array_to_base64(hist_image)
            processed_list.append(getHeader(extension) + str(hist_img64))
            pre_img_list.append(getHeader(extension) + img)
            processed_histograms.append(getHeader() + str(histogram_of_post_img))
            pre_img_histograms.append(getHeader() + str(histogram_of_pre_img))
            return_size = (str(m)+str(w) + ' pixels')
            if i == len(pre_img) - 1 and i > 0:
                # we need to zip
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                zipped_list = b64_strings_to_b64_zip(processed_list, extension)
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size,
                    "b64_zip_out": getHeader(".zip") + zipped_list
                }
                make_tmp(new_info)
                return jsonify(new_info),200
            elif i == len(pre_img) - 1 and i == 0:
                # we don't need to zip. single image
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size
                }
                make_tmp(new_info)
                return jsonify(new_info),200
        elif method == "Reverse Video":
            if jpgFileNum == 0:
                os.chmod('images',stat.S_IRWXU)
                os.makedirs(('images/'+str(email)))
                os.chmod(('images/'+str(email)),stat.S_IRWXU)
            jpgFileNum = jpgFileNum + 1
            filename = 'images/'+str(email)+'/'+str(jpgFileNum)+'.jpg'
            with open(filename, "wb") as image_out:
                image_out.write(base64.b64decode(img))
            iSave = save_image(email, jpgFileNum)
            iRev = add_rever(email)
            imgArray, a_type, m, w, z = convert_image_to_np_array(img)
            hist_image = reverseVid(img)
            histogram_of_pre_img = create_histo(imgArray)
            histogram_of_post_img = create_histo(hist_image)
            hist_img64 = convert_processed_np_array_to_base64(hist_image)
            processed_list.append(getHeader(extension) + str(hist_img64))
            pre_img_list.append(getHeader(extension) + img)
            processed_histograms.append(getHeader() + str(histogram_of_post_img))
            pre_img_histograms.append(getHeader() + str(histogram_of_pre_img))
            return_size = (str(m)+str(w) + ' pixels')
            if i == len(pre_img) - 1 and i > 0:
                # we need to zip
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                zipped_list = b64_strings_to_b64_zip(processed_list, extension)
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size,
                    "b64_zip_out": getHeader(".zip") + zipped_list
                }
                make_tmp(new_info)
                return jsonify(new_info),200
            elif i == len(pre_img) - 1 and i == 0:
                # we don't need to zip. single image
                new_time = datetime.datetime.now()
                duration = new_time - current_time
                new_info = {
                    "user_email": email,
                    "proc_method": method,
                    "pre_b64_string": pre_img_list,
                    "post_b64_string": processed_list,
                    "pre_histogram": pre_img_histograms,
                    "post_histograms": processed_histograms,
                    "action_time": str(duration),
                    "upload_time": time2str(current_time),
                    "pic_size": return_size
                }
                make_tmp(new_info)
                return jsonify(new_info),200


@app.route("/download", methods=["GET"])
def download():
    # access tmp folder and output
    output = access_tmp()
    return jsonify(output)
