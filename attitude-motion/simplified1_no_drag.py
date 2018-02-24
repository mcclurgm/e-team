import numpy as np
import scipy.integrate as integrate
import time

# I did all the integrations and solving ODEs by hand. I do not have forces
# or anything else in here. I will take a photo of my work to check the math.
# we should calibrate the angle to account for nonzero initial angle that doesn't move
class Localizer():

    def __init__(self):
        self.prop_mass = .056
        self.drone_mass = 1.518
        self.mass = self.drone_mass + self.prop_mass
        self.g = 9.80655

        # given pos, velocity from last round

        self.vx = 0
        self.vy = 0
        self.x = 0
        self.y = 0

        self.cur_time = time.time()

    # Udpates instance variables for position and velocity
    # using Euler's method, with dt as time since last update
    # Intended to be executed every time a new data set arrives from the drone
    def update(self, pitch, roll):
        time_step = time.time() - self.cur_time
        vx0 = self.vx
        vy0 = self.vy

        self.vx = self.final_velocity(vx0, time_step, pitch)
        self.x = self.final_position(self.x, vx0, time_step, pitch)

        self.vy = self.final_velocity(vy0, time_step, roll)
        self.y = self.final_position(self.y, vy0, time_step, pitch)
    
    # time step in seconds
    def update(self, pitch, roll, time_step):
        vx0 = self.vx
        vy0 = self.vy

        self.vx = self.final_velocity(vx0, time_step, pitch)
        self.x = self.final_position(self.x, vx0, time_step, pitch)

        self.vy = self.final_velocity(vy0, time_step, roll)
        self.y = self.final_position(self.y, vy0, time_step, pitch)

    # Get velocity and position after a specified time interval
    # These methods get exact values from physical theory (no numerical approximation)
    # but they are drastic simplifications of that theory and have a lot of error.. 
    # x0, v0 are values at the beginning of the iteration. They are not Euler FPA values.
    # These are independent of each other. Position can be found with final_position only.
    # final_velocity is only used to get v values for other computation
    # this takes 10^-5 s to execute.
    def final_velocity(self, v0, time_step, angle):
        # acceleration = g * tan(angle)
        return v0 + self.g * np.tan(angle) * time_step

    def final_position(self, x0, v0, time_step, angle):
        return x0 + (v0 * time_step) + ((self.g * np.tan(angle)) / 2) * (time_step**2) 

    # for testing results against Mathematica
    def test_at_time(self, time_step, angle):
        print self.vx + time_step * self.g * np.tan(angle)

    def test_with_time_step(self, pitch, roll, time_step):
        # time_step = time.time() - self.cur_time
        vx0 = 0
        vy0 = 0
        x0 = 0
        y0 = 0

        self.vx = self.final_velocity(vx0, time_step, pitch)
        self.x = self.final_position(x0, vx0, time_step, pitch)

        self.vy = self.final_velocity(vy0, time_step, roll)
        self.y = self.final_position(y0, vy0, time_step, pitch)
    
    def test_with_real_time(self, pitch, roll):
        time_step = time.time() - self.cur_time
        vx0 = 0
        vy0 = 0
        x0 = 0
        y0 = 0

        self.vx = self.final_velocity(vx0, time_step, pitch)
        self.x = self.final_position(self.x, vx0, time_step, pitch)

        self.vy = self.final_velocity(vy0, time_step, roll)
        self.y = self.final_position(self.y, vy0, time_step, pitch)

def test(thing):
    for i in range(0,101):
        print str(i) + ": "
        now = time.time()
        thing.test_with_time_step(np.pi/4, np.pi/4, i)
        print time.time() - now

        print thing.vx
        print thing.x
        print ""

def test_with_real_time(thing):
    begin = time.time()
    prev = time.time()
    # print begin - prev
    now = time.time()
    # print begin - now
    while now - begin < 11:
        prev = now
        now = time.time()
        print now - begin
        thing.test_with_real_time(np.pi/4, np.pi/4)
        print thing.vx
        print thing.x

        time.sleep(1.00000)
    print now - begin

# thing1 = Localizer()
# print thing1.cur_time
# test(thing1)
# test_with_real_time(thing1)