## Event handlers for gesture events
from time import time

def tempoChangeAction(controller, bpm):
    print "Received tempo %f " % bpm 
    controller.midi_interface.set_tempo(bpm)
    #controller.update('handleTempoChange')

def trackStartAction(controller, tracknum=1):
    print "Start Track"
    controller.midi_interface.play_track(tracknum)
    controller.stopped = False

def trackStopAction(controller, tracknum=1):
    print "Stop Track"
    controller.midi_interface.stop_track(tracknum)
    controller.stopped = True

def lowerVolumeAction(controller, vol=0.5):
    tracknum = 1
    volume = controller.current_vol - vol
    print "Lower Volume: %d" % volume
    controller.midi_interface.vol_track(tracknum, volume)
    controller.current_vol = volume

def raiseVolumeAction(controller, vol=0.5):
    tracknum = 1
    volume = controller.current_vol+ vol
    print "Raise Volume: %d" % volume
    controller.midi_interface.vol_track(tracknum, volume)
    controller.current_vol = volume

def stopAllAction(controller):
    print "Stop All"
