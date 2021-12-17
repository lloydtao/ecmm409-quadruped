from constants import FRAME_RATE, LENGTH_OF_SIMULATION
from pyrosim import pyrosim

import numpy as np
import pybullet as p
import pybullet_data


class Motor:
    def __init__(self, jointName, amplitude, frequency):
        self.jointName = jointName
        self.amplitude = amplitude * 500
        self.frequency = frequency

    def set_value(self, n, robotId):
        rate = FRAME_RATE / self.frequency
        if n % rate > 0 and n % rate < rate / 4:
            pyrosim.Set_Motor_For_Joint(
                bodyIndex=robotId,
                jointName=self.jointName,
                controlMode=p.POSITION_CONTROL,
                targetPosition=np.pi / 4.0,
                maxForce=self.amplitude,
            )
        else:
            pyrosim.Set_Motor_For_Joint(
                bodyIndex=robotId,
                jointName=self.jointName,
                controlMode=p.POSITION_CONTROL,
                targetPosition=0,
                maxForce=self.amplitude,
            )
