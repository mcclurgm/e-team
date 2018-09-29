#!/usr/bin/env python3

import numpy as np
import scipy.integrate as integrate
import time
print(('hello', 'there'))

a = np.array([[0.],
                 [-5.66181428],
                 [ 9.80655   ]])
v = np.array([[0.],
                 [0.],
                 [0.]])
r = np.array([[0.],
                 [0.],
                 [0.]])

def func(q, t, acceleration):
    q1 = q[1]                 # q1' = q2
    q2 = acceleration.item(1) # q2' = a
    return [q1, q2]

def vector_func(q, t, acceleration):
    q1 = q[1]         # q1' = q2
    q2 = acceleration # q2' = a
    return [q1, q2]

a_t = [0, 1]
t = time.time()
# sol = integrate.odeint(func, [0, 0], a_t, args=(a,))
sol = integrate.odeint(func, [0, 0], a_t, args=(a,))
print('Time to use ODE solver: {0}'.format(time.time() - t))
print(sol)