from sklearn import svm
import features
import pickle
import utils

feature_generators = [
    features.average_velocity,
]

class GestureLearner:
    def __init__(self):
        self.classifier = svm.LinearSVC()
        self.feature_vectors = []
        self.classifications = []

    def get_feature_vector(self,gesture):
        """
            Calculate a vector of features for the given gesture
        """
        vector = []
        for generator in feature_generators:
            vector.append(generator(gesture))

        return [i for i in utils.flatten(vector)]

    def register_data(self,gestures,classifications):
        """
            Generate a list of feature vectors and train the classifier on them
        """
        feature_vectors = []

        for gesture in gestures:
            vector = self.get_feature_vector(gesture)
            feature_vectors.append(vector)

        self.feature_vectors += feature_vectors
        self.classifications += classifications

    def learn(self):
        self.classifier.fit(self.feature_vectors,self.classifications)

    def predict(self,gesture):
        """
            Predict a classification for the given feature
        """
        vector = self.get_feature_vector(gesture)
        return self.classifier.predict([vector])[0]

    def save_classifier(self,filename="classifier.pickle"):
        """
            Save the classifier to a file
        """
        with open(filename,"w") as f:
            pickle.dump(self.classifier,f)

    def load_data(self,filename="data.pickle"):
        """
            Load the classifier from a file
        """
        with open(filename,"r") as f:
            self.feature_vectors,self.classifications = pickle.load(f)

    def save_data(self,filename="data.pickle"):
        """
            Save the classifier to a file
        """
        with open(filename,"w") as f:
            pickle.dump([self.feature_vectors,self.classifications],f)
