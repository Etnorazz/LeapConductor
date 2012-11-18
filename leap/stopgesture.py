from lib import Leap

class StopAllListener(Leap.Listener):
    """
    Stop EVERYTHING!
    A right->left swipe with closed fist.
    """
    def __init__(self, callback, controller):
        self.controller = controller
        self.callback = callback
        super(StopAllListener, self).__init__()

    def onInit(self, controller): 
        self.prev_vel = []
        self.alpha = 0.3
        self.previousVelocity = 0

    def onFrame(self, controller): 
        frame = controller.frame()
        hand = frame.hands()
        numHands = len(hand)

        if numHands >= 1: 
            hand = hand[0]
            numFingers = len(hand.fingers()) 
            if hand.velocity() != None: 
                self.previousVelocity = (1-self.alpha)*self.previousVelocity + self.alpha*hand.velocity().x
            else: 
                self.previousVelocity = 0
            if numFingers == 0 and self.shouldAppend(self.previousVelocity): 
                self.prev_vel.append("")
                if len(self.prev_vel) > 200:
                    print len(self.prev_vel), 
                    self.prev_vel = []
                    self.callback(self.controller)
            else: 
                self.prev_vel = []
                self.previosVelocity = 0

    def shouldAppend(self, vel): 
        return vel > 300



