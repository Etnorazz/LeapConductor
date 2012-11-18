from lib import Leap
import sys
import math
import time
from utils import *

class TempoRecognizer:
    def __init__(self,callback, controller):
        self.average_velocity = Leap.Vector(0,0,0)
        self.angle_history = []
        self.velocity_history = []

        self.changing = False

        self.last_change_time = None
        self.bpm = 0

        self.callback = callback
        self.controller = controller

        #settings
        self.default_alpha = .3 #for the kalman filters
        self.threshold_angle = .7
        self.threshold_speed = .1

    def change(self,alpha = None,debug = False):
        if not alpha:
            alpha = self.default_alpha
        if self.last_change_time:
            delta = time.time() - self.last_change_time
            if delta > self.threshold_speed:
                self.bpm = (1-alpha)*self.bpm + alpha*(30/delta)
                self.callback(self.controller, self.bpm)
                if debug:
                    print "BPM:",self.bpm

        self.last_change_time = time.time()

    def update_velocity(self,velocity,alpha = None):
        if not alpha:
            alpha = self.default_alpha

        n = norm(self.average_velocity)*norm(velocity)
        if n>=0.01:
            angle = dot(self.average_velocity,velocity)/(n)
            if angle<self.threshold_angle:
                if not self.changing:
                    self.change()
                self.changing = True
            else:
                self.changing = False
            self.angle_history.append(angle)

        self.average_velocity = add(mul(self.average_velocity,(1-alpha)),mul(velocity,alpha))
        self.velocity_history.append(norm(self.average_velocity))

    def register_frame(self,frame):
        hands = frame.hands()
        if len(hands)>0:
            hand = hands[0]
            fingers = hand.fingers()
            if len(fingers)>0:
                finger = fingers[0]

                posistion = finger.tip().position
                velocity = finger.velocity()

                self.update_velocity(velocity)
