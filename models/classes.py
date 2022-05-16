import fuzzy_systems.fs_pneumonia_client
import fuzzy_systems.fs_tuberculosis
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


def get_subclasses_names():
    class_names = []

    for subclass in AbstractModel.__subclasses__():
        class_names.append(subclass.__name__)

    return class_names


class AbstractModel:
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def cnn_model_path(self):
        return self.__cnn_model_path

    @cnn_model_path.setter
    def cnn_model_path(self, cnn_model_path):
        self.__cnn_model_path = cnn_model_path

    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, classes):
        self.__classes = classes

    def get_fuzzy_result(self, symptoms):
        return None

    def get_cnn_prediction(self, filepath):
        cnn_model = load_model(self.cnn_model_path)
        classes = self.classes

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

    def __init__(self):
        self.__name = None
        self.__cnn_model_path = None
        self.__classes = None


class Pneumonia(AbstractModel):
    def __init__(self):
        super().__init__()
        self.name = 'Pneumonia'
        self.cnn_model_path = 'cnn_models/pneumonia_categorical.h5'
        self.classes = ['normal', 'pneumonia_bacteria', 'pneumonia_virus']

    def get_fuzzy_result(self, symptoms):
        return fuzzy_systems.fs_pneumonia_client.get_fuzzy_pneumonia_result(symptoms)


class Tuberculosis(AbstractModel):
    def __init__(self):
        super().__init__()
        self.name = 'Tuberculosis'
        self.cnn_model_path = 'cnn_models/tuberculosis_categorical.h5'
        self.classes = ['normal', 'tuberculosis']

    def get_fuzzy_result(self, symptoms):
        return fuzzy_systems.fs_tuberculosis.get_fuzzy_tuberculosis_result(symptoms)
