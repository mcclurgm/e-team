import numpy as np
import scipy.integrate as integrate

# I did all the integrations and solving ODEs by hand. I do not have forces
# or anything else in here. I will take a photo of my work to check the math.
class Localizer():

    def __init__(self):
        self.mass = 1.99
        self.g = 9.80655

        # given pos, velocity from last round

        self.vx = 0
        self.vy = 0
        self.x = 0
        self.y = 0

    def update(self, pitch, roll):
        self.vx = final_velocity(v0, cur_time - last_time, pitch)
        self.x = final_position(x0, v0, cur_time - last_time, pitch)

        self.vy = final_velocity(v0, cur_time - last_time, roll)
        self.y = final_position(x0, v0, cur_time - last_time, pitch)

    def final_velocity(self, v0, time_step, angle):
        return v0 + time_step * self.g * np.tan(angle)

    def final_position(self, x0, v0, time_step, angle):
        return x0 + (v0 * time_step) + (self.g  * (time_step**2) * np.tan(angle) / 2)

thing1 = Localizer()
test(thing1)
def test(thing):
    for i in range(0,101):
        print str(i) + ": "
        thing.update(np.pi/4, np.pi/4)
        print thing.vx
        print thing.x
        print ""
