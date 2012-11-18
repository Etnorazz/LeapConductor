from lib import Leap
import sys 
from learn import collect, learn

class LearnedListener(Leap.Listener): 

    def __init__(self, callback, controller): 
        super(StartTrackListener, self).__init__()
        self.callback = callback 
        self.controller = controller

    def onInit(self, controller): 
        self.learner = learn.GestureLearner()
        self.learner.load_data()
        self.learner.load_classifier()

        self.max_length = self.learner.max_length
        self.window = []

    def onFrame(self, controller): 
        self.window.append(controller.frame())
        if len(self.window) > self.max_length:
            self.window.pop(0)

        
