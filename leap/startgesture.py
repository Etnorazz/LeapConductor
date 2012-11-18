from lib import Leap
import sys 

class StopTrackListener(Leap.Listener): 

    def __init__(self, callback, controller): 
        super(StopTrackListener, self).__init__()
        self.callback = callback 
        self.controller = controller
        
    def onInit(self, controller): 
        self.previousStops = []
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
            if numFingers < 1 and self.previousVelocity < 200: 
                self.previousStops.append("one")
                if len(self.previousStops) > 20:
                    self.callback(self.controller)
            else: 
                self.previousStops = []

class LowerVolumeListener(Leap.Listener): 

    def __init__(self, callback, controller): 
        super(LowerVolumeListener, self).__init__()
        self.callback = callback 
        self.controller = controller

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
                self.previousVelocity = (1-self.alpha)*self.previousVelocity + self.alpha*hand.velocity().y
            else: 
                self.previousVelocity = 0
            if numFingers > 1 and self.shouldAppend(self.previousVelocity): 
                self.prev_vel.append("")
                if len(self.prev_vel) > 20:
                    self.callback(self.controller)
            else: 
                self.prev_vel = []
                self.previosVelocity = 0

    def shouldAppend(self, vel): 
        return vel > 200

class RaiseVolumeListener(LowerVolumeListener): 

    def shouldAppend(self, vel): 
        return vel < -200
