from constants import FRAME_RATE, LENGTH_OF_SIMULATION
from pyrosim import pyrosim

import numpy as np
import pybullet as p
import pybullet_data


class Motor:
    def __init__(self, jointName, amplitude, frequency):
        """Initialise a motor, which powers a joint between two blocks.

        Args:
            jointName (string): Name of the joint as stated in the generated model.
            amplitude (int): Force of the joint, which will be multiplied by 500 Newton-meters (Nm).
            frequency (int): How many times the joint will fire in the simulation.
        """
        self.jointName = jointName
        self.amplitude = amplitude * 500
        self.frequency = frequency

    def set_value(self, n, robotId):
        """Tell the joint where it is meant to be.

        Args:
            n (int): Physics simulation frame number.
            robotId (int): ID of the model in which to manipulate this joint.
        """
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
