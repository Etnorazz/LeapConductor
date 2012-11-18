from lib import Leap
from abletonactions import *
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
        # (callback, recognizer, default value, timeout)
        'tempoChange': (handleTempoChange, TempoRecognizer, 97.19, float('inf')),
        'volumeUp': (handleVolumeUp, LowerVolume, 0, float('inf')),
        'volumeDown': (handleVolumeDown, RaiseVolume, 0, float('inf')),
    }
    last_change = {
    }


    def __init__(self, gestures, period = 60):
        self.midi_interface = MidiInterface()
        self.recognizers = []
        self.period = period

        print "Initializing a recognizer"
        for g_name in gestures:
            callback = AbletonController.supported_gestures[g_name][0]
            recognizer = AbletonController.supported_gestures[g_name][1]
            self.recognizers.append((g_name, recognizer(callback, self)))
            AbletonController.last_change[g_name] = time.time()
        
        self.kill = threading.Event()
        self.dispatch_thread = None

    def update(self, name):
        AbletonController.last_change[name] = time.time()

    # dispacth the frames in a batch
    def dispatch(self, frame=None):
        for name,r in self.recognizers:
            r.register_frame(frame)
        if not self.dispatch_thread:
            self.initDefaults()

    # for each handler that has timed out, fire the default event
    def dispatchDefaults(self):
        for r, v in AbletonController.supported_gestures.items():
            timeout = v[3]
            if time.time() - AbletonController.last_change[r] > timeout:
                AbletonController.last_change[r] = time.time()
                callback = v[0]
                callback(self, v[2])


    # at intervals, fire default values to any handlers who have timed out
    def flush(self, kill, period):
        print "flush initialized"
        while True:
            kill.wait(1.0/period)
            if kill.isSet():
                break
            self.dispatchDefaults()
    
    def initDefaults(self):
        self.dispatch_thread = threading.Thread(target=self.flush, args=(self.kill, self.period))
        self.dispatch_thread.start()

    def stop(self):
        self.kill.set()


        


    
