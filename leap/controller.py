from lib import leap
from abletonactions import AbletonAction as actions
from gestures import Gesture

# Query gesture information and communicate with Ableton
# to control music

class AbletonController:
    """

    """
    supported_gestures = {
        'trackStart': actions.trackStartAction,
        'trackStop': actions.trackStopAction,
        'songStop': actions.songStopAction,
        'songStart': actions.songStartAction,
        'tempoUp': actions.tempoUpAction,
        'tempoDown': actions.tempoDownAction,
        'volumeUp': actions.volumeUpAction,
        'volumeDown': actions.volumeDownAction
    }
    def __init__(self, gestures):
        self.gestures = []
        for g_name in gestures:
            g = Gesture(g_name, supported_gestures[g_name])
            self.gestures.append(g)
    


    
