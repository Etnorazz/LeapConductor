from lib import Leap
from abletonactions import *
from gestures import TempoRecognizer

# Query gesture information and communicate with Ableton
# to control music

class AbletonController:
    """

    """
    supported_gestures = {
        'tempoChange': (handleTempoChange, TempoRecognizer),
    }


    def __init__(self, gestures):
        self.recognizers = []
        for g_name in gestures:
            recognizer = AbletonController.supported_gestures[g_name][1](AbletonController.supported_gestures[g_name])
            self.recognizers.append(recognizer)
            print "Initialized a recognizer for %s" % g_name

    def dispatch(self, frame):
        for r in self.recognizers:
            r.register_frame(frame)
        


    
