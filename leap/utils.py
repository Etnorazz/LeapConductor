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
def subtract(vec1,vec2):
    return add(vec1,mul(vec2,-1))
def collapse(vec):
    return abs(vec.x)+abs(vec.y)+abs(vec.z)

def average_position(vectors):
    ave_x = ave([v.x for v in vectors])
    ave_y = ave([v.y for v in vectors])
    ave_z = ave([v.z for v in vectors])
    return Leap.Vector(ave_x,ave_y,ave_z)

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el
