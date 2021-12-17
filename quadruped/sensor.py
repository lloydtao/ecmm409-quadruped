from constants import FRAME_RATE, LENGTH_OF_SIMULATION
from pyrosim import pyrosim

import numpy as np
import pybullet as p


class Sensor:
    def __init__(self, linkName):
        """Initialise a sensor.

        Args:
            linkName (string): Name of the generated model's respective block.
        """
        self.linkName = linkName
        self.value = -1
        self.values = np.zeros(FRAME_RATE * LENGTH_OF_SIMULATION)

    def get_value(self, n):
        """Detect the measured value and store it.

        Args:
            n (int): Physics simulation frame number.

        Returns:
            int: Value of the reading.
        """
        self.value = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        self.values[n] = self.value

        return self.value
