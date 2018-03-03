# Notes for redoing this with matrices and vectors in numpy

## Rotation matrices
```python
# rotation about z axis
yaw_rotation = np.matrix([np.cos(alpha), -np.sin(alpha), 0],
                         [np.sin(alpha), np.cos(alpha), 0],
                         [0, 0, 1])

# rotation about y axis (forward/back)
pitch_rotation = np.matrix([np.cos(beta), 0, -np.sin(beta)],
                           [0, 1, 0],
                           [-np.sin(beta, 1, np.cos(beta)])

# rotation about x axis (side-to-side)
roll_rotation = np.matrix([1, 0, 0],
                          [0, np.cos(alpha), -np.sin(gamma)],
                          [0, np.sin(gamma), np.cos(gamma)])
```

Standard procedure: roll, then pitch, then yaw  
Using matrix multiplication