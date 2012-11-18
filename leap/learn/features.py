### From a series of frames, extract useful features
## Features:
# Average of the first n derivatives
# Percentage time for each finger configuration
#
import numpy as np
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt
from matplotlib import cm

def feature1(frames):
    """
    Average of the first derivative
    """
    w = np.random.rand(100)*4.0-2.0
    x = np.random.rand(100)*4.0-2.0
    y = np.random.rand(100)*4.0-2.0
    z = x*np.exp(-x**2-y**2-w**2)
    ti = np.linspace(-2.0, 2.0, 100)
    WI, XI, YI = np.meshgrid(ti, ti)

    rbf = Rbf(w, x, y, z, epsilon=2)
    ZI = rbf(XI, YI)

    n = plt.normalize(-2., 2.)
    plt.subplot(1,1,1)
    plt.pcolor(XI, YI, ZI, cmap=cm.jet)
    plt.scatter(x, y, 100, z, cmap=cm.jet)
    plt.title('RBF interpolation - multiquadrics')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.colorbar()
    plt.show()

feature1([])


def feature2(frames):
    """
    Average of the second derivative
    """
    pass

def feature3(frames):
    """
    Average of the third derivative
    """
    pass

def feature4(frames):
    pass
