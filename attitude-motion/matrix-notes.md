# Notes for redoing this with matrices and vectors in numpy

## Rotation matrices
```python
yaw_rotation = np.array([[np.cos(alpha), -np.sin(alpha), 0],
                         [np.sin(alpha), np.cos(alpha), 0],
                         [0, 0, 1]])

# rotation about y axis (forward/back)
pitch_rotation = np.array([[np.cos(beta), 0, np.sin(beta)],
                           [0, 1, 0],
                           [-np.sin(beta), 0, np.cos(beta)]])

# rotation about x axis (side-to-side)
roll_rotation = np.array([[1, 0, 0],
                          [0, np.cos(gamma), -np.sin(gamma)],
                          [0, np.sin(gamma), np.cos(gamma)]])
```

Standard procedure: roll, then pitch, then yaw  (yaw * pitch * roll)
Using matrix multiplication

```python
total_rotation = np.dot(np.dot(yaw_rotation, pitch_rotation), roll_rotation)
rotated_unit = np.dot(total_rotation, thrust_unit)
```

## The physics
Rotation matrix converts pitch/roll axes to universal coordinates  
TBD how doing the physics will work with this matrix form  
I should look at Nyla's code to see what she did about this

* Multiply total_rotation by vector {0,0,1}: isolate right column
  * `rotated_unit`
* Solve formula `u_z * f == m * a` for `f`
* Scale force unit vector

```python
vert = rotated_unit[2]
f = (m * g) / vert
f_vector = f * rotated_unit
```

* Should I rename rotated_unit to f_hat?
* Yay?

## Integration options
### `scipy.integrate.solve_ivp()`

### Attempt to do this by hand...
```
x = x0 + v0t + Integrate[a(t),{t,0,tf},{t,0,tf}]
```