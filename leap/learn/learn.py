from sklearn import svm
from learn import features
import pickle
import utils

feature_generators = [
    features.length,
    features.average_position,
    features.average_velocity,
]

class GestureLearner:
    def __init__(self):
        self.classifier = svm.SVC()

    def get_feature_vector(self,gesture):
        """
            Calculate a vector of features for the given gesture
        """
        vector = []
        for generator in feature_generators:
            vector.append(generator(gesture))

        return utils.flatten(vector)

    def learn(self,gestures,classifications):
        """
            Generate a list of feature vectors and train the classifier on them
        """
        feature_vectors = []
        for gesture in gestures:
            vector = self.get_feature_vector(gesture)
            feature_vectors.append(vector)

        self.classifier.fit(feature_vectors,classifications)

    def predict(self,gesture):
        """
            Predict a classification for the given feature
        """
        vector = get_feature_vector(gesture)
        self.classifier.predict(vector)

    def load(self,filename="data.pickle"):
        """
            Load the classifier from a file
        """
        with open(filename,"r") as f:
            self.classifier = pickle.load(f)

    def save(self,filename="data.pickle"):
        """
            Save the classifier to a file
        """
        with open(filename,"w") as f:
            pickle.dump(self.classifier,f)
