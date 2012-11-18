from lib import Leap

class TestListener(Leap.Listener): 

    def __init__(self, callback, controller): 
        super(TestListener, self).__init__()
        self.callback = callback 
        self.controller = controller

    def onInit(self, controller): 
        self.prev_vel = []
        self.alpha = 0.3
        self.previousVelocity = 0

    def onFrame(self, controller): 
        frame = controller.frame()
        hands = frame.hands()
        numHands = len(hands)

        if numHands >= 1: 
            for hand in hands:
                numFingers = len(hand.fingers()) 
                if numFingers > 1:
                    if hand.velocity() != None: 
                        self.previousVelocity = (1-self.alpha)*self.previousVelocity + self.alpha*hand.velocity().x
                    else: 
                        self.previousVelocity = 0
                    if self.shouldAppend(self.previousVelocity): 
                        self.prev_vel.append("")
                        if len(self.prev_vel) > 10:
                            print numFingers, "fingers and ", numHands, "hands"
                            print self.previousVelocity, len(self.prev_vel)
                            self.prev_vel = []
                            self.callback(self.controller)
                    else: 
                        self.prev_vel = []
                        self.previosVelocity = 0

    def shouldAppend(self, vel): 
        return vel > 200

