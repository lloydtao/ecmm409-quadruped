from constants import FRAME_RATE, LENGTH_OF_SIMULATION
from pyrosim import pyrosim

import numpy as np
import pybullet as p


class Sensor:
    def __init__(self, linkName):
        self.linkName = linkName
        self.value = -1
        self.values = np.zeros(FRAME_RATE * LENGTH_OF_SIMULATION)

    def get_value(self, n):
        self.value = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        self.values[n] = self.value

        return self.value
