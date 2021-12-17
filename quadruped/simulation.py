from constants import FRAME_RATE, LENGTH_OF_SIMULATION
from pyrosim import pyrosim
from quadruped import Quadruped
from world import World

import math
import numpy as np
import pybullet as p
import pybullet_data
import time


class Simulation:
    def __init__(self, realtime=False):
        """Initialise physics server and load models."""
        physicsClient = p.connect(p.GUI)
        p.setGravity(0, 0, -9.8 * 3)
        self.realtime = realtime

        self.world = World()
        self.quadruped = Quadruped()

    def run(self):
        """Run loop of environment interactions."""
        for i in range(FRAME_RATE * LENGTH_OF_SIMULATION):
            # Update model physics in client
            p.stepSimulation()
            if self.realtime:
                time.sleep(1 / FRAME_RATE)

            # Load model actions for next step
            self.world.step(i)
            self.quadruped.step(i)

        position = p.getLinkState(self.quadruped.robotId, 0)[0][0]
        return position


if __name__ == "__main__":
    s = Simulation(realtime=True)
    s.run()
    p.disconnect()
