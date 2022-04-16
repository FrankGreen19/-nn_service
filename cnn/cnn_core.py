from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from models.classes import AbstractModel
from models.classes import Pneumonia
from models.classes import Tuberculosis


def get_cnn_prediction(filepath, illness):
    model_class = globals()[illness]
    model_ins = model_class()
    if not isinstance(model_ins, AbstractModel):
        return False

    cnn_model = load_model(model_ins.cnn_model_path)
    classes = model_ins.classes

    img = image.load_img(filepath, target_size=(150, 150), color_mode="rgb")
    x = image.img_to_array(img)
    x = x.reshape(-1, 150, 150, 3)

    prediction = cnn_model.predict(x).tolist()[0]

    i = 0
    for diagnosis in prediction:
        if diagnosis == 1:
            prediction = classes[i]
        i += 1

    return prediction

