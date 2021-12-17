from constants import FRAME_RATE, LENGTH_OF_SIMULATION
from pyrosim import pyrosim
from sensor import Sensor
from motor import Motor

import numpy as np
import pybullet as p
import pybullet_data


class Quadruped:
    def __init__(self):
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
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = Sensor(linkName)

    def sense(self, n):
        for _, sensor in self.sensors.items():
            v = sensor.get_value(n)

    def prepare_to_act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = Motor(jointName, 1, 1)

    def act(self, n):
        for _, motor in self.motors.items():
            v = motor.set_value(n, self.robotId)

    def step(self, n):
        self.sense(n)
        self.act(n)
