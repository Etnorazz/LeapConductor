from lib import Leap
import sys 
"""
def main(): 
    listener = StopTrackListener() 
    controller = Leap.Controller(listener) 

    raiseListener = RaiseVolumeListener() 
    raiseController = Leap.Controller(raiseListener)

    lowerListener = LowerVolumeListener() 
    lowerController = Leap.Controller(lowerListener) 


    print "Press Enter to quit" 
    sys.stdin.readline() 

    controller = None
"""

class StopTrackListener(Leap.Listener): 

    def __init__(self, callback, controller):
        self.controller = controller 
        self.callback = callback

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
                if len(self.previousStops) > 8:
                    self.previousStops = []
                    self.callback(self.controller)
            else: 
                self.previousStops = []

class LowerVolumeListener(Leap.Listener): 
    def __init__(self, callback, controller):
        self.controller = controller 
        self.callback = callback

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
                if len(self.prev_vel) > 4:
                    self.callback(self.controller)
                    self.prev_vel = []
            else: 
                self.prev_vel = []
                self.previosVelocity = 0

    def shouldAppend(self, vel): 
        return vel > 200

class RaiseVolumeListener(LowerVolumeListener): 

    def shouldAppend(self, vel): 
        return vel < -200
