from werkzeug.utils import secure_filename
import os
from services import file_validator
from cnn import cnn_core

# def get_xray_result():
#     result = 'undefined'
#     # requestData = request.get_json()
#     # answerData = requestData['data']
#
#     file = request.files['image']
#     filename = secure_filename(file.filename)
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     file.save(filepath)
#     result = cnn_core.get_cnn_prediction(filepath, 'Tuberculosis')
#
#     return {"answer": result}
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
