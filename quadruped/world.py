import pybullet as p
import pybullet_data


class World:
    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        planeId = p.loadURDF("plane.urdf")

    def step(self, n):
        pass
