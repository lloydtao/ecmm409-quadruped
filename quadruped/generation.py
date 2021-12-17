from pyrosim import pyrosim


class Generation:
    def create_robot(legs=([0.5, 0.5, 1], [0.5, 0.5, 1])):
        pyrosim.Start_URDF("models/body.urdf")

        torso_size = [1, 1, 1]
        torso_pos = [0, 0, 1.5]

        torso_frontleg_joint = [0.5, 0, 1]

        frontleg_size = legs[0]
        frontleg_pos = [
            frontleg_size[0] / 2,
            0,
            frontleg_size[2] / 2 - frontleg_size[2],
        ]

        torso_backleg_joint = [-0.5, 0, 1]

        backleg_size = legs[1]
        backleg_pos = [
            backleg_size[0] / 2 * -1,
            0,
            backleg_size[2] / 2 - backleg_size[2],
        ]

        pyrosim.Send_Cube(name="Torso", pos=torso_pos, size=torso_size)

        pyrosim.Send_Cube(name="FrontLeg", pos=frontleg_pos, size=frontleg_size)

        pyrosim.Send_Joint(
            name="Torso_FrontLeg",
            parent="Torso",
            child="FrontLeg",
            type="revolute",
            position=" ".join(str(x) for x in torso_frontleg_joint),
        )

        pyrosim.Send_Cube(name="BackLeg", pos=backleg_pos, size=backleg_size)

        pyrosim.Send_Joint(
            name="Torso_BackLeg",
            parent="Torso",
            child="BackLeg",
            type="revolute",
            position=" ".join(str(x) for x in torso_backleg_joint),
        )

        pyrosim.End()


if __name__ == "__main__":
    Generation.create_robot()
