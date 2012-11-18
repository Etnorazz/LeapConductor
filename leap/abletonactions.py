## Event handlers for gesture events
from time import time

def tempoChangeAction(controller, bpm):
    print "Received tempo %f " % bpm 
    controller.midi_interface.set_tempo(bpm)
    controller.update('handleTempoChange')

def __init__():
    pass

def trackStartAction():
    pass

def trackStopAction(controller):
    print "Stop Track"

def songStartAction():
    pass

def songStopAction():
    pass

def handleVolumeUp(controller, vol=2):
    tracknum = 1
    volume = controller.current_vol+ vol
    controller.midi_interface.vol_track(tracknum, volume)

def handleVolumeDown(controller, vol=2):
    tracknum = 1
    volume = controller.current_vol - vol
    controller.midi_interface.vol_track(tracknum, volume)

def lowerVolumeAction(controller):
    print "Lower Volume"

def raiseVolumeAction(controller):
    print "Raise Volume"

def stopAllAction(controller):
    print "Stop All"
