import json
from services import db_service

jVal = '{"D":"true","xray_img_path":"images\\/jNCLDLR1ug.jpg","medical_test_id":53,"async_job_id":48}'
parameters = json.loads(jVal)

symptoms = dict
for parameter in parameters:
    if parameters[parameter] == 'true':
        symptoms.fromkeys(parameter, parameters[parameter])

xrayPath = parameters["xray_img_path"]
medicalTest = parameters["medical_test_id"]

result = db_service.get_async_job(parameters["async_job_id"])
print(result['id'])


