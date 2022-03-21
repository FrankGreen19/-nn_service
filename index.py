from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from modules import file_validator
from cnn import cnn_core
from fuzzy import pneumonia

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploaded_images"

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


@app.route('/get-xray-result', methods=['POST'])
def get_xray_result():
    result = 'undefined'
    # requestData = request.get_json()
    # answerData = requestData['data']

    file = request.files['image']
    if file and file_validator.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        result = cnn_core.get_cnn_prediction(filepath)

    return {"answer": result}


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
    bt = request.form['bt']
    a = request.form['a']
    bun = request.form['bun']
    rr = request.form['rr']
    bp = request.form['bp']
    hr = request.form['hr']
    ab = request.form['ab']
    su = request.form['su']
    ss = request.form['ss']
    sg = request.form['sg']

    fuzzy_result = float(pneumonia.get_fuzzy_result(bt, a, bun, rr, bp, hr, ab, su, ss, sg)['PP'])

    file = request.files['image']
    if file and file_validator.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        cnn_result = cnn_core.get_cnn_prediction(filepath)

    result = ""
    if ((cnn_result == 'normal' and fuzzy_result >= 35)
            or ((cnn_result == 'pneumonia_bacteria' or cnn_result == 'pneumonia_virus') and fuzzy_result < 35)):
        result = "Обнаружены признаки пневмонии, рекомендуется обратиться к специалисту!"
    elif cnn_result == 'normal' and fuzzy_result < 15:
        result = "Вы здоровы, все в порядке"
    else:
        result = "Обнаружена пневмония, немедленно обратитесь к специалисту!"

    fuzzy_result = float(format(fuzzy_result, '.2f'))

    if fuzzy_result <= 34:
        fuzzy_result = str(fuzzy_result) + " (низкая вероятность)"
    elif 35 <= fuzzy_result <= 74:
        fuzzy_result = str(fuzzy_result) + " (средняя вероятность)"
    else:
        fuzzy_result = str(fuzzy_result) + " (высокая вероятность)"

    return render_template('index.html', result=result, cnn_result=cnn_result, fuzzy_result=fuzzy_result)


if __name__ == "__main__":
    app.run(debug=True)
