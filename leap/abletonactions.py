## Event handlers for gesture events

def __init__():
    pass

def trackStartAction():
    pass

def tempoChangeAction(controller, bpm):
    print "Received tempo %f " % bpm 
    controller.midi_interface.set_tempo(bpm)

def trackStopAction(controller):
    print "Stop Track"

def songStartAction():
    pass

def songStopAction():
    pass

def lowerVolumeAction(controller):
    print "Lower Volume"

def raiseVolumeAction(controller):
    print "Raise Volume"
