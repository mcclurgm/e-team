import dronekit_sitl
import numpy as np
import scipy.integrate as integrate

"""
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

print vehicle.attitude # returns in radians

vehicle.close()

sitl.stop()
print("Completed")
"""

mass = 1.99
g = 9.80655

def net_horizontal_force_from_angle_simplified(angle):
    Fg = -1 * mass * g

    # Ft = force of thrust
    # Ftx = (Fg cos(theta)) / sin(theta) = Fg tan(theta)
    Ft = -1 * Fg * (1 / np.cos(angle))
    Ftx = Ft * np.sin(angle)
    return Ftx

    # alternate, simplified form to be used if I don't want to reuse Ft
    Ftx = Fg * np.tan(angle)
    return Ftx

def get_acceleration(force, angle, mass): # angle in radians, using np.pi as pi
    a = g * (1 / np.tan(angle))
    return a

def final_velocity_simplified(v0, accel, time_step, angle):
    return v0 + time_step * g * np.tan(angle)

def final_position_simplified(x0, v0, time_step, angle):
    return x0 + (v0 * time_step) + (g  * (time_step**2) * np.tan(angle) / 2)

def update_horizontal_position_velocity(force, mass, time_step):
    # assumes constant net force over interval
    a = force / mass

    # velocity
    final = integrate.quad()

    #position

def update_velocity(v, a, t):
    return v0 + (a * t)

def update_position(pos0, v, t):
    return x0 + (a * t)

print net_horizontal_force_from_angle_simplified(np.pi / 6)
