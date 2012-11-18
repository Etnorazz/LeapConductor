## Event handlers for gesture events
from time import time

def handleTempoChange(controller, bpm):
    print "Received tempo %f " % bpm 
    controller.midi_interface.set_tempo(bpm)
    controller.update('handleTempoChange')

def __init__():
    pass

def trackStartAction():
    pass

def trackStopAction():
    pass

def songStartAction():
    pass

def songStopAction():
    pass

def handleVolumeUp(controller, ):
    pass

def volumeDownAction():
    pass
