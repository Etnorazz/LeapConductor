import math
from lib import Leap

def dot(vec1,vec2):
    return vec1.x*vec2.x + vec1.y*vec2.y + vec1.z*vec2.z
def norm(vec):
    return math.sqrt(vec.x*vec.x + vec.y*vec.y + vec.z*vec.z)
def mul(vec,a):
    return Leap.Vector(vec.x*a,vec.y*a,vec.z*a)
def add(vec1,vec2):
    return Leap.Vector(vec1.x+vec2.x, vec1.y+vec2.y, vec1.z*vec2.z)
