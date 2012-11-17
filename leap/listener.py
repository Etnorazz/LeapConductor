from lib import Leap
import sys
<<<<<<< HEAD
from controller import AbletonController

class LeapListener(Leap.Listener):

    def __init__(self, gestures):
        super(Leap.Listener, self).__init__()
        self.ableton_controller = AbletonController(gestures)
        print "Created an AbletonController supporting gestures:"
        for g in gestures:
            print g
    
=======
from gestures import GestureRecognizer

class LeapListener(Leap.Listener):
    def __init__(self,*args,**kwargs):
        super(LeapListener,self).__init__(*args,**kwargs)
        self.gr = GestureRecognizer()
>>>>>>> 7d126dc88ca0b315e4917235b7afe0abb1f03e34
    def onInit(self, controller):
        print "Initialized"

    def onConnect(self, controller):
        print "Connected"

    def onDisconnect(self, controller):
        print "Disconnected"

    def onFrame(self,controller):
        self.gr.register_frame(controller.frame())

def main():
    # Create a sample listener and assign it to a controller to receive events
    listener = LeapListener()
    controller = Leap.Controller(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    sys.stdin.readline()
    print "Showing"
    listener.gr.freeze()
    listener.gr.show()

    # The controller must be disposed of before the listener
    controller = None

if __name__=="__main__":
    main()
