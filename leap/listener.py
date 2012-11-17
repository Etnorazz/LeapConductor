from lib import Leap
import sys
from gestures import GestureRecognizer

class LeapListener(Leap.Listener):
    def __init__(self,*args,**kwargs):
        super(LeapListener,self).__init__(*args,**kwargs)
        self.gr = GestureRecognizer()
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
