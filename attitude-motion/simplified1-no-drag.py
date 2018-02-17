import numpy as np
import scipy.integrate as integrate

# I did all the integrations and solving ODEs by hand. I do not have forces
# or anything else in here. I will take a photo of my work to check the math.

mass = 1.99
g = 9.80655

def final_velocity(v0, time_step, angle):
    return v0 + time_step * g * np.tan(angle)

def final_position(x0, v0, time_step, angle):
    return x0 + (v0 * time_step) + (g  * (time_step**2) * np.tan(angle) / 2)

def test():
    for i in range(0,101):
        print str(i) + ": "
        print final_velocity(0,i,np.pi/4)
        print final_position(0,0,i,np.pi/4)
        print ""

test()