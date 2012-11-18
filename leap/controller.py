from lib import Leap
from abletonactions import *
from tempo import TempoRecognizer

# Query gesture information and communicate with Ableton
# to control music

class AbletonController:
    """

    """
    supported_gestures = {
        'tempoChange': (handleTempoChange, TempoRecognizer),
    }


    def __init__(self, gestures):
        #self.midi_interface = MidiInterface()
        self.recognizers = []
        for g_name in gestures:
            callback = AbletonController.supported_gestures[g_name][0]
            recognizer = AbletonController.supported_gestures[g_name][1]
            self.recognizers.append(recognizer(callback, self))
            print "Initialized a recognizer for %s" % g_name

    def dispatch(self, frame):
        for r in self.recognizers:
            r.register_frame(frame)
        


    
