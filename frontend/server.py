from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/simple", methods=["POST"])
def imgStr():
    """
    Returns image string
    """
    r = request.get_json()
    b64_string = r["b64_string"]
    user_email = r["user_email"]
    proc_method = r["proc_method"]
    data = {
        "user_id": user_email,
        "image_string": b64_string,
        "processing_tech": proc_method
    }
    return jsonify(data)
