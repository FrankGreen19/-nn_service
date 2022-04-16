class AbstractModel:

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

    def __init__(self):
        self.__cnn_model_path = None
        self.__classes = None


class Pneumonia(AbstractModel):
    def __init__(self):
        super().__init__()
        self.cnn_model_path = 'cnn_models/pneumonia_categorical.h5'
        self.classes = ['normal', 'pneumonia_bacteria', 'pneumonia_virus']


class Tuberculosis(AbstractModel):

    def __init__(self):
        super().__init__()
        self.cnn_model_path = 'cnn_models/tuberculosis_categorical.h5'
        self.classes = ['normal', 'tuberculosis']
