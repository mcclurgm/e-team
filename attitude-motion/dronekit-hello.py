print "Start simulator (SITL)"
import dronekit_sitl
import numpy as np

''' sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

print vehicle.attitude

vehicle.close()

sitl.stop()
print("Completed")
 '''
mass = 1.99
g = 9.80655

def net_force():
    fg = mass * g
    

def get_acceleration(force, angle, mass): # angle in radians, using np.pi as pi
    a = g * (1 / np.tan(angle))
    return a

def update_velocity(v0, a, t):
    return v0 + (a * t)

def update_position(pos0, v, t):
    return x0 + (a * t)
