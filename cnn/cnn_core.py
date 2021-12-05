from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model('cnn/pneumonia_cnn.h5')

classes = ['normal', 'pneumonia']


def getCnnPrediction(filepath):
    img = image.load_img(filepath, target_size=(150, 150), color_mode="rgb")
    x = image.img_to_array(img)
    x = x.reshape(-1, 150, 150, 3)

    prediction = model.predict(x)

    return classes[int(prediction)]

