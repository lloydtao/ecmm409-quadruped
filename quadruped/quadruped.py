from constants import FRAME_RATE, LENGTH_OF_SIMULATION
from pyrosim import pyrosim
from sensor import Sensor
from motor import Motor

import numpy as np
import pybullet as p
import pybullet_data


class Quadruped:
    def __init__(self):
        """Initialise the walker."""
        self.motors = {}
        self.sensors = {}

        # Load model
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.robotId = p.loadURDF("models/body.urdf")

        # Prepare sensors
        pyrosim.Prepare_To_Simulate("models/body.urdf")
        self.prepare_to_sense()
        self.prepare_to_act()

    def prepare_to_sense(self):
        """Register sensors within the walker."""
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = Sensor(linkName)

    def sense(self, n):
        """Tell each sensor to read and store its detected value.

        Args:
            n (int): Physics simulation frame number.
        """
        for _, sensor in self.sensors.items():
            v = sensor.get_value(n)

    def prepare_to_act(self):
        """Register motors within the walker."""
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = Motor(jointName, 1, 1)

    def act(self, n):
        """Tell each motor to do what it's meant to do at this frame.

        Args:
            n (int): Physics simulation frame number.
        """
        for _, motor in self.motors.items():
            v = motor.set_value(n, self.robotId)

    def step(self, n):
        """Detect sensor values and fire motors accordingly.

        Args:
            n (int): Physics simulation frame number.
        """
        self.sense(n)
        self.act(n)
