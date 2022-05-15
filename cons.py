import json
from services import db_service
from fuzzy_systems import fs_pneumonia_client, fs_tuberculosis
import requests
import os
from dotenv import load_dotenv
from cnn import cnn_core

load_dotenv()

jVal = '{"symptoms":[{"CP":"true","C":"true","D":"true","BT":36.6,"A":70,"F":"false", "H":"true", "DA":"true"}],"xray_img_name":"jNCLDLR1ug.jpg","test_type":"common","medical_test_id":8,"async_job_id":49}'
messageContext = json.loads(jVal)

fuzzyResult = dict()
cnnResult = dict()

asyncJobId = messageContext["async_job_id"]

if messageContext['test_type'] == 'common':
    fuzzyResult['pneumonia_fuzzy'] = fs_pneumonia_client.get_fuzzy_pneumonia_result(messageContext['symptoms'][0])
    fuzzyResult['tuberculosis_fuzzy'] = fs_tuberculosis.get_fuzzy_tuberculosis_result(messageContext['symptoms'][0])

    imagePath = os.getenv('FILE_UPLOAD_DIR') + messageContext['xray_img_name']

    binaryFile = requests.get(os.getenv('API_DOWNLOAD_FILE_URL'), params={'imageName': messageContext['xray_img_name']})
    with open(imagePath, 'wb') as writableFile:
        writableFile.write(binaryFile.content)

    cnnResult['tuberculosis_cnn'] = cnn_core.get_cnn_prediction(imagePath, 'Tuberculosis')
    cnnResult['pneumonia_cnn'] = cnn_core.get_cnn_prediction(imagePath, 'Pneumonia')

    db_service.update_medical_test(messageContext["medical_test_id"], fuzzyResult=json.dumps(fuzzyResult),
                                   cnnResult=json.dumps(cnnResult))

    os.remove(imagePath)
    db_service.update_async_job_status(asyncJobId, 'completed')


