import numpy as np
from numpy import cos, sin

class Localizer():
    def __init__(self):
        self.prop_mass = .056
        self.drone_mass = 1.518
        self.m = self.drone_mass + self.prop_mass
        self.g = 9.80655

        self.base_thrust_unit = np.array([[0],[0],[1]])

    def get_force_vector(self, yaw, pitch, roll):
        f_hat = self.f_hat(yaw, pitch, roll)
        print f_hat
        return self.get_force_magnitude(f_hat) * f_hat

    def get_force_magnitude(self, f_hat):
        f_z = f_hat[2]
        print f_z
        f = (self.m * self.g) / f_z
        # f_vector = f * f_hat
        return f
    
    def f_hat(self, yaw, pitch, roll):
        return np.dot(self.total_rotation(yaw, pitch, roll), self.base_thrust_unit)
    
    def total_rotation(self, alpha, beta, gamma):
        yaw_rotation = np.array([[np.cos(alpha), -np.sin(alpha), 0],
                                    [np.sin(alpha), np.cos(alpha), 0],
                                    [0, 0, 1]])
        pitch_rotation = np.array([[np.cos(beta), 0, np.sin(beta)],
                                [0, 1, 0],
                                [-np.sin(beta), 0, np.cos(beta)]])
        roll_rotation = np.array([[1, 0, 0],
                                [0, np.cos(gamma), -np.sin(gamma)],\
                                [0, np.sin(gamma), np.cos(gamma)]])
        return np.dot(np.dot(yaw_rotation, pitch_rotation), roll_rotation)

    def test(self):
        f_hat = self.f_hat(0, 0, np.pi/6)
        # print f_hat

        # print self.get_force_magnitude(f_hat)

        f = self.get_force_vector(0, 0, np.pi/6)
        print f

localizer = Localizer()
localizer.test()