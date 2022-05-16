import json
from services import db_service
import requests
import os
from dotenv import load_dotenv
from models import classes
from models.classes import Pneumonia
from models.classes import Tuberculosis

load_dotenv()

jVal = '{"symptoms":[{"CP":"true","C":"true","D":"true","BT":36.6,"A":70,"F":"false", "H":"true", "DA":"true"}],"xray_img_name":"jNCLDLR1ug.jpg", "test_type":"Pneumonia","medical_test_id":8,"async_job_id":49}'
messageContext = json.loads(jVal)

asyncJobId = messageContext["async_job_id"]
testType = messageContext['test_type']
symptoms = messageContext['symptoms'][0]

illnessList = []
illnessClassList = []
if testType == 'all':
    illnessList = classes.get_subclasses_names()
else:
    illnessList.append(testType)

fuzzyResults = dict()
for illness in illnessList:
    illnessClass = globals()[illness]
    illnessInst = illnessClass()
    illnessClassList.append(illnessInst)
    fuzzyResults[illness] = illnessInst.get_fuzzy_result(symptoms)

imagePath = os.getenv('FILE_UPLOAD_DIR') + messageContext['xray_img_name']
cnnResults = dict()
if imagePath:
    binaryFile = requests.get(os.getenv('API_DOWNLOAD_FILE_URL'), params={'imageName': messageContext['xray_img_name']})

    if binaryFile.status_code == 200:
        with open(imagePath, 'wb') as writableFile:
            writableFile.write(binaryFile.content)

        for illness in illnessClassList:
            cnnResults[illness.name] = illness.get_cnn_prediction(imagePath)
            print('hi')

        os.remove(imagePath)
    else:
        print('error')  # @todo logs
        db_service.update_async_job_status(asyncJobId, 'failed')
        exit()

db_service.update_medical_test(messageContext["medical_test_id"], fuzzyResult=json.dumps(fuzzyResults),
                               cnnResult=json.dumps(cnnResults))

db_service.update_async_job_status(asyncJobId, 'completed')
