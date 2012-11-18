from lib import Leap
import sys
from controller import AbletonController
from tempo import TempoRecognizer

def f(a):
    pass
class LeapListener(Leap.Listener):
    def __init__(self):
        print "wtf"
        super(LeapListener,self).__init__()
        #self.controller = AbletonController(gestures)

    def onInit(self, controller):
        print "Initialized"

    def onConnect(self, controller):
        print "Connected"

    def onDisconnect(self, controller):
        print "Disconnected"

    def onFrame(self,controller):
        #self.controller.dispatch(controller.frame())
        frame = controller.frame()
        hands = frame.hands()
        if len(hands) > 0:
            hand = hands[0]
            fingers = hand.fingers()
            print len(hands), len(fingers)

def main():
    # Create a sample listener and assign it to a controller to receive events
    #listener = LeapListener(['tempoChange', ])#'volumeUp', 'volumeDown'])
    listener = LeapListener()
    controller = Leap.Controller(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    sys.stdin.readline()

    # The controller must be disposed of before the listener
    controller = None

if __name__=="__main__":
    main()

