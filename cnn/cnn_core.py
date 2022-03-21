from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model('cnn/pneumonia_categorical.h5')

classes = ['Признаков пневномонии на снимке не обнаружено', 'Бактериальная пневмония', 'Вирусная пневмония']


def get_cnn_prediction(filepath):
    img = image.load_img(filepath, target_size=(150, 150), color_mode="rgb")
    x = image.img_to_array(img)
    x = x.reshape(-1, 150, 150, 3)

    prediction = model.predict(x).tolist()[0]

    i = 0
    for diagnosis in prediction:
        if diagnosis == 1:
            prediction = classes[i]
            break
        i += 1

    return prediction

