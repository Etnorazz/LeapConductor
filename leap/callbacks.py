## Event handlers for gesture events
from time import time

def handleTempoChange(controller, bpm):
    print "Received tempo %f " % bpm 
    controller.midi_interface.set_tempo(bpm)
    controller.update('handleTempoChange')

def trackStartAction():
    pass

def trackStopAction():
    pass

def songStartAction():
    pass

def handleStopTrack(controller, ):
    pass

def handleVolumeUp(controller, vol=2):
    tracknum = 1
    volume = controller.current_vol+ vol
    controller.midi_interface.vol_track(tracknum, volume)

def handleVolumeDown(controller, vol=2):
    tracknum = 1
    volume = controller.current_vol - vol
    controller.midi_interface.vol_track(tracknum, volume)
