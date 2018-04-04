import numpy as np
from numpy import cos, sin

# rotation about z axis
def yaw_rotation(vector, alpha):
    yaw_rotation = np.array([[np.cos(alpha), -np.sin(alpha), 0],
                             [np.sin(alpha), np.cos(alpha), 0],
                             [0, 0, 1]])
    return np.dot(yaw_rotation, vector)

# rotation about y axis (forward/back)
def pitch_rotation(beta):
    pitch_rotation = np.array([[np.cos(beta), 0, np.sin(beta)],
                               [0, 1, 0],
                               [-np.sin(beta), 0, np.cos(beta)]])
    return np.dot(pitch_rotation, vector)

# rotation about x axis (side-to-side)
def roll_rotation(vector, gamma):
    roll_rotation = np.array([[1, 0, 0],
                              [0, np.cos(gamma), -np.sin(gamma)],\
                              [0, np.sin(gamma), np.cos(gamma)]])
    return np.dot(roll_rotation, vector)

thrust_unit = np.array([[0],[0],[1]])

alpha = 0
beta = 0
gamma = np.pi/4

yaw_rotation = np.array([[np.cos(alpha), -np.sin(alpha), 0],
                            [np.sin(alpha), np.cos(alpha), 0],
                            [0, 0, 1]])
pitch_rotation = np.array([[np.cos(beta), 0, np.sin(beta)],
                           [0, 1, 0],
                           [-np.sin(beta), 0, np.cos(beta)]])
roll_rotation = np.array([[1, 0, 0],
                          [0, np.cos(gamma), -np.sin(gamma)],\
                          [0, np.sin(gamma), np.cos(gamma)]])

total_rotation = np.dot(np.dot(yaw_rotation, pitch_rotation), roll_rotation)
rotated_unit = np.dot(total_rotation, thrust_unit)
