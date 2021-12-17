import pybullet as p
import pybullet_data


class World:
    def __init__(self):
        """Initialise the world, which is a large plane."""
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        planeId = p.loadURDF("plane.urdf")

    def step(self, n):
        """Run one physics engine iteration. This is currently static.

        Args:
            n (int): Physics simulation frame number."""
        pass
