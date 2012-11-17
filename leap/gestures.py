from lib import Leap
import sys
import math

class MotionState:
    def __init__(self):
        self.position = Leap.Vector(0,0,0)
        self.velocity = Leap.Vector(0,0,0)
        self.acceleration = Leap.Vector(0,0,0)
        self.angular_change = 0

def dot(vec1,vec2):
    return vec1.x*vec2.x + vec1.y*vec2.y + vec1.z*vec2.z
def norm(vec):
    return math.sqrt(vec.x*vec.x + vec.y*vec.y + vec.z*vec.z)
def mul(vec,a):
    return Leap.Vector(vec.x*a,vec.y*a,vec.z*a)
def add(vec1,vec2):
    return Leap.Vector(vec1.x+vec2.x, vec1.y+vec2.y, vec1.z*vec2.z)
def threshold(l,value):
    for i in l:
        if abs(i) > value:
            yield value * i/abs(i)
        else:
            yield 0

class GestureRecognizer:
    def __init__(self):
        self.average_velocity = Leap.Vector(0,0,0)
        self.angle_history = []
        self.velocity_history = []
        self._freeze = False

    def freeze(self):
        self._freeze = True
    def update_velocity(self,velocity,alpha = .3):
        n = norm(self.average_velocity)*norm(velocity)
        if n>=0.01:
            angle = dot(self.average_velocity,velocity)/(n)
            self.angle_history.append(angle)

        self.average_velocity = add(mul(self.average_velocity,(1-alpha)),mul(velocity,alpha))
        self.velocity_history.append(norm(self.average_velocity))

    def register_frame(self,frame):
        if self._freeze:
            return
        hands = frame.hands()
        if len(hands)>0:
            hand = hands[0]
            fingers = hand.fingers()
            if len(fingers)>0:
                finger = fingers[0]

                posistion = finger.tip().position
                velocity = finger.velocity()

                self.update_velocity(velocity)
    def show(self):
        import matplotlib.pyplot as plt
        x = range(len(self.velocity_history))
        y = self.velocity_history

        x2 = range(len(self.angle_history))
        y2 = [abs(i) for i in threshold(self.angle_history,.8)]

        #plt.plot(x,y)
        #plt.show()
        plt.plot(x2,y2)
        plt.show()
