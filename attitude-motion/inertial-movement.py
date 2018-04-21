import numpy as np
import scipy.integrate as integrate
from numpy import cos, sin
import time

class Localizer():
    def __init__(self):
        self.prop_mass = .056
        self.drone_mass = 1.518
        self.m = self.drone_mass + self.prop_mass
        self.g = 9.80655

        self.base_thrust_unit = np.array([[0],[0],[1]])
        
        self.v = np.array([[0],[0],[0]])
        self.r = np.array([[0],[0],[0]])
    
    # Attempting to implement double integrals, since the first method is wrong
    def double_update(self, yaw, pitch, roll, time_step):
        f = self.force_vector(yaw, pitch, roll)
        a = f / self.m

        v = self.vector_integrate(a, self.v, time_step)
        print('v')
        print(v)

        r = self.double_integrate(a, self.r, self.v, time_step)
        print('r')
        print(r)

        self.v = v
        self.r = r

    def update(self, yaw, pitch, roll, time_step):
        f = self.force_vector(yaw, pitch, roll)
        a = f / self.m

        v = self.vector_integrate(a, self.v, time_step)
        print('v')
        print(v)
        self.v = v

        r = self.vector_integrate(v, self.r, time_step)
        print('r')
        print(r)
        self.r = r

    # This agrees with Mathematica, I think. If the Mathematica way of doing it is right.
    def double_integrate(self, vector, initial_outer, initial_inner, time_step):
        result_list = []
        for i in range(0, len(vector)):
            component_func = lambda q, t: vector[i]
            double_result = integrate.dblquad(component_func, 0, time_step, lambda t: 0, lambda t: t)
            # integrate() returns tuple with result as 0, error as 1
            component = double_result[0] + (initial_inner[i] * time_step) + initial_outer[i]
            result_list.append(component)
        result_vector = np.array(result_list)
        return result_vector
    
    def vector_integrate(self, vector, initial, time_step):
        result_list = []
        for i in range(0, len(vector)):
            component_func = lambda t: vector[i]
            component_integrate = integrate.quad(component_func, 0, time_step)
            # integrate() returns tuple with result as 0, error as 1
            component = component_integrate[0] + initial[i]
            result_list.append(component)
        result_vector = np.array(result_list)
        return result_vector
    
    def euler(self, yaw, pitch, roll, time_step):
        a = self.force_vector(yaw, pitch, roll) / self.m
        vn = self.v + (a * time_step)
        rn = self.r + (self.v * time_step)

        self.v = vn
        self.r = rn

    def force_vector(self, yaw, pitch, roll):
        f_hat = self.f_hat(yaw, pitch, roll)
        # print(f_hat)
        return self.get_force_magnitude(f_hat) * f_hat

    def get_force_magnitude(self, f_hat):
        f_z = f_hat[2]
        # print f_z
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

    def position(self):
        return self.r
    
    def velocity(self):
        return self.v

    def test(self):
        yaw = 0
        pitch = 0
        roll = np.pi / 6
        f_hat = self.f_hat(yaw, pitch, roll)
        # print f_hat

        # print self.get_force_magnitude(f_hat)

        f = self.force_vector(yaw, pitch, roll)
        # self.update(yaw, pitch, roll, 0.05)
        # return

        t = 0
        for i in range(0, 20):
            self.double_update(yaw, pitch, roll, 0.05)
            t += 0.05
            # print(self.position())
        print('total time {0}'.format(t))
        a = self.force_vector(yaw, pitch, roll) / self.m
        v = self.vector_integrate(a, [0,0,0], 1.0)
        print('Total integrated v {0}'.format(v))
        r = self.double_integrate(a, [0,0,0], [0,0,0], 1.0)
        print('Total integrated r {0}'.format(r))

localizer = Localizer()
localizer.test()