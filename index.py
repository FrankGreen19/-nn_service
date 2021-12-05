from flask import Flask, request
from werkzeug.utils import secure_filename
import os
from modules import file_validator
from cnn import cnn_core

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploaded_images"

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


@app.route('/get-xray-result', methods = ['POST'])
def getXrayResult():
    result = 'undefined'
    # requestData = request.get_json()
    # answerData = requestData['data']

    file = request.files['image']
    if file and file_validator.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        result = cnn_core.getCnnPrediction(filepath)

    return {"answer": result}


if __name__ == "__main__":
    app.run(debug=True)