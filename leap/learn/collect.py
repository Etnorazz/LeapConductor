import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
from lib import Leap 

class Listener(Leap.Listener): 
    def __init__(self): 
        self.recording = False
        super(Listener, self).__init__()

    def onInit(self, controller): 
        self.frames = []

    def onFrame(self, controller): 
        if self.recording: 
            self.frames.append(controller.frame())
    def start_recording(self): 
        self.recording = True

    def stop_recording(self): 
        self.recording = False 
        return_list = self.frames 
        self.frames = [] 
        return return_list

def listen(gesture_list): 
    listener = Listener() 
    controller = Leap.Controller(listener) 

    print "Press Enter to toggle recording" 
    print "Press q + Enter to quit"
    print ">>",
    while True: 
        letter = sys.stdin.readline()
        if letter[0]  == 'q': 
            gesture_list.append(listener.stop_recording())
            print "Done recognizing gesture"
            print ">>",
            break
        if listener.recording: 
            print "Stoping record" 
            print ">>",
            gesture_list.append(listener.stop_recording())
        else: 
            print "Starting record"
            print ">>",
            listener.start_recording()

print """Hello, welcome to the gesture learner, please enter one of the following options: 
    learn - Learn a new gesture 
    recognize - Let the program guess what you are trying to input 
    q - Quit""" 
print ">>",
while True: 
    command = sys.stdin.readline()
    if "learn" in command: 
        print "Enter the name of the gesture: ", 
        gesture_name = sys.stdin.readline()
        gesture_list = []
        listen(gesture_list)

        """gLearner = GestureLearner() 
        gLearner.learn(gesture_list) 
        gLearner.save()"""
    elif "recognize" in command: 
        print "recognize" 
        print ">>", 
    elif command[0] == "q": 
        print "Goodbye"
        break
    else: 
        print """Unrecognized command, usage:
learn - Learn a new gesture 
recognize - Let the program guess what you are trying to input 
q - Quit""" 
        print ">>",
