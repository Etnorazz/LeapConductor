import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 
from lib import Leap 
from learn.learn import GestureLearner

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
        return_list = [frame for frame in self.frames]
        self.frames = [] 
        return return_list

def listen(gesture_list): 
    listener = Listener() 
    controller = Leap.Controller(listener) 

    print "Press Enter to toggle recording" 
    print "Press q + Enter to quit"
    print "Enter to start recording",
    while True: 
        letter = sys.stdin.readline()
        if letter[0]  == 'q': 
            print "Done recognizing gesture"
            print "Enter Command: ",
            break
        if listener.recording: 
            print "Stoping record" 
            print "Enter to start recording",
            gesture_list.append(listener.stop_recording())
        else: 
            print "Starting record"
            print "Recording...",
            listener.start_recording()

def guess(gLearner): 
    gesture_list = []
    print "Press Enter to start recgnizing",
    listener = Listener() 
    controller = Leap.Controller(listener)
    letter = sys.stdin.readline()
    listener.start_recording()
    sys.stdin.readline()
    gesture_list = listener.stop_recording()
    import binascii
    print binascii.unhexlify(hex(gLearner.predict(gesture_list))[2:])


print """Hello, welcome to the gesture learner, please enter one of the following options: 
        learn - Learn a new gesture 
        recognize - Let the program guess what you are trying to input 
        q - Quit""" 
print "Enter Command: ",

gLearner = GestureLearner() 
while True: 
    command = sys.stdin.readline()
    if "learn" in command: 
        print "Enter the name of the gesture: ", 
        import binascii 
        gesture_name = int(binascii.hexlify(sys.stdin.readline().lower()), 16)
        gesture_list = []
        listen(gesture_list)

        gLearner.register_data(gesture_list, [gesture_name for i in gesture_list])
        gLearner.save_data()
    elif "recognize" in command: 
        gLearner.learn()
        guess(gLearner)     
        print "Enter Command: ", 
    elif command[0] == "q": 
        print "Goodbye"
        break
    elif "load" in command: 
        gLearner.load_data() 
        print "Enter Command: ",
    else: 
        print """Unrecognized command, usage:
        learn - Learn a new gesture 
        recognize - Let the program guess what you are trying to input 
        q - Quit""" 
        print "Enter Command: ",
