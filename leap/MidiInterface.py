import socket
import sys
import math

class MidiInterface():
    def __init__(self, port=20000, host=''):
        self.HOST = host
        self.PORT = port
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST, self.PORT)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def send(self, data):
            self.sock.sendto(data, self.ADDR)
    def set_tempo(self, bpm):
        x = bpm-20
        x = int(math.floor(x/7.709))
        self.send("/tempo %d" % x)
        
