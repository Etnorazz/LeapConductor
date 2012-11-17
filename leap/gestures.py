import Leap

class LeapListener(Leap.Listener):
    def onInit(self, controller):
        print "Initialized"

    def onConnect(self, controller):
        print "Connected"

    def onDisconnect(self, controller):
        print "Disconnected"

    def onFrame(self,controller):
        print "Frame"

def main():
    # Create a sample listener and assign it to a controller to receive events
    listener = LeapListener()
    controller = Leap.Controller(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    sys.stdin.readline()

    # The controller must be disposed of before the listener
    controller = None

if __name__=="__main__":
    main()
