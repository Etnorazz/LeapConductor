from lib import leap
from abletonactions import AbletonAction as actions
from gestures import TempoRecognizer

# Query gesture information and communicate with Ableton
# to control music

class AbletonController:
    """

    """
    supported_gestures = {
        'tempoChange': actions.tempoChange,
    }

    supported_recognizers = {
        'tempoChange': TempoRecognizer,
    }

    def __init__(self, gestures):
        self.recognizers = []
        for g_name in gestures:
            recognizer = AbletonController.supported_recognizers[g_name](AbletonController.supported_gestures[g_name])
            self.gestures.append(recognizer)
            print "Initialized a recognizer for %s" % g_name
        


    
