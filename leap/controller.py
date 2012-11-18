from lib import Leap
from abletonactions import *

from tempo import TempoListener
from startgesture import *
from starttrack import *
from testlistener import *

from MidiInterface import *
import threading, time

# Query gesture information and communicate with Ableton
# to control music

class AbletonController:
    """
    """
    supported_gestures = {
        'tempoChange': (tempoChangeAction, TempoListener),
        'stopTrack': (trackStopAction, StopTrackListener),
        'lowerVolume': (lowerVolumeAction, LowerVolumeListener),
        'raiseVolume': (raiseVolumeAction, RaiseVolumeListener),
        'startTrack': (trackStartAction, StartTrackListener),
        #'test': (trackSt
    }


    def __init__(self):
        self.midi_interface = MidiInterface()
        self.recognizers = []
        self.controllers = []

        self.current_vol = 90
        self.stopped = False

        for g_name in AbletonController.supported_gestures.keys():
            callback = AbletonController.supported_gestures[g_name][0]
            recognizer = AbletonController.supported_gestures[g_name][1]

            r = recognizer(callback, self)
            self.recognizers.append(r)
            self.controllers.append(Leap.Controller(r))
            print "Initialized a recognizer for %s" % g_name

    def destroy(self):
        for index,c in self.controllers.enumerate():
            self.controllers = None
