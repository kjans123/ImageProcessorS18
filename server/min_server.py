from flask import Flask, jsonify, request
from flask_cors import CORS
import base64
import numpy as np
import PIL
from PIL import Image
import stat
import os

app = Flask(__name__)
CORS(app)


@app.route("/process", methods=["POST"])
def process():
    r = request.get_json()
    pre_img = r["pre_b64_string"]
    for i in len(range(pre_img)):
        decoded_string = base64.b64decode(pre_img[i])
        with open('temp2.jpg', 'wb') as f:
            f.write(decoded_string)
        f.close()
        os.chmod('temp2.jpg', stat.S_IRWXU)
        i = Image.open('temp2.jpg')
        msgString = "IT WORKS!!"
    return_dict = {
        "work_msg": msgString
                  }
    return jsonify(return_dict), 200
