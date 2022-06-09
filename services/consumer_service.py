import json
from services import db_service
import requests
import os
from dotenv import load_dotenv
from models import classes
from models.classes import Pneumonia
from models.classes import Tuberculosis

load_dotenv()


def consume(messageBody):
    messageContext = json.loads(messageBody)
    asyncJobId = messageContext["async_job_id"]

    try:
        testType = messageContext['test_type']
        symptoms = messageContext['symptoms']

        illnessList = []
        illnessClassList = []
        if testType == 'Common':
            illnessList = classes.get_subclasses_names()
        else:
            illnessList.append(testType)

        fuzzyResults = dict()
        for illness in illnessList:
            illnessClass = globals()[illness]
            illnessInst = illnessClass()
            illnessClassList.append(illnessInst)
            fuzzyResults[illness] = illnessInst.get_fuzzy_result(symptoms)

        cnnResults = dict()
        if 'xray_img_name' in messageContext:
            imagePath = os.getenv('FILE_UPLOAD_DIR') + messageContext['xray_img_name']

            binaryFile = requests.get(os.getenv('API_DOWNLOAD_FILE_URL'),
                                      params={'imageName': messageContext['xray_img_name']})

            if binaryFile.status_code == 200:
                with open(imagePath, 'wb') as writableFile:
                    writableFile.write(binaryFile.content)

                for illness in illnessClassList:
                    cnnResults[illness.name] = illness.get_cnn_prediction(imagePath)

                os.remove(imagePath)
            else:
                print('error')  # @todo logs
                db_service.update_async_job_status(asyncJobId, 'failed')
                exit()

        db_service.update_medical_test(messageContext["medical_test_id"], fuzzyResults=fuzzyResults,
                                       cnnResults=cnnResults)

        db_service.update_async_job_status(asyncJobId, 'completed')
    except BaseException as e:
        # @todo logs
        db_service.update_async_job_status(asyncJobId, 'failed')
