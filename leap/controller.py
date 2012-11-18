from lib import Leap
from callbacks import *
from tempo import TempoRecognizer
from startgesture import *
from MidiInterface import *
import threading, time

# Query gesture information and communicate with Ableton
# to control music

class AbletonController:
    """

    """
    supported_gestures = {
        # (callback, recognizer)
        'tempoChange': (handleTempoChange, TempoRecognizer), 
        'volumeUp': (handleVolumeUp, LowerVolumeListener),
        'volumeDown': (handleVolumeDown, RaiseVolumeListener),
        'stopTrack': (handleVolumeDown, RaiseVolumeListener)
    }


    def __init__(self, gestures, period = 60):
        self.midi_interface = MidiInterface()
        self.recognizers = []
        self.period = period

        self.current_vol = 108.0

        print "Initializing a recognizer"
        for g_name in gestures:
            callback = AbletonController.supported_gestures[g_name][0]
            recognizer = AbletonController.supported_gestures[g_name][1]
            self.recognizers.append((g_name, recognizer(callback, self)))
