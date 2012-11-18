from sklearn import svm
from learn import features

feature_generators = [
    features.feature1, 
]

def learn(gestures,classifications):
    #generate the feature vectors from the gestures
    feature_vectors = []
    for gesture in gestures:
        vector = []
        for generator in feature_generators:
            vector.append(generator(gesture))
        feature_vectors.append(vector)

    classifier = svm.SVC()
    classifier.fit(feature_vectors,classifications)
