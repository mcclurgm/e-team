## Altitude sensor
Should I use z acceleration only? Is that gained using derivatives that would then accumulate a lot of error?

I could take the absolute position and correct my values. If I get my z to not match somehow, I might be able to correct my change vectors. Who knows?
* If I would update the change vectors, then that would involve breaking them out into a separate thing and then adding initial conditions somehow. I'm worried that could be really complicated.
* Would that mean that I should just solve these together somehow? I'm already thinking about that and this could be another reason.
  - It seems like you can't break initial conditions out of the vectors. I could for v, but r depends on the conditions for v in an inner integral, at least as it is right now.

## Integration: ODEs
* I should probably use this because it will be reusable once I do acceleration, which is not cleanly separable

### `odeint` (old version)
* [https://nathantypanski.com/blog/2014-08-23-ode-solver-py.html]
* Put in terms of first order diffeqs only
* r''(t) = a
  - Define q1 = r
  - q2 = r'
  - So q1' = q2
  - q2' = a
  - Alternatively, call q1 = r; q2 = v
* So the python function is...
```python
def func(q, t):
    q1 = q[1] # q1' = q2
    q2 = a    # q2' = a
    return [q1, q2]
```
  - This will return an array of [q1, q2] or [r, r']

* My numbers:

```python
a = [[0.],
    [-5.66181428],
    [ 9.80655   ]]

def func(q, t):
    q1 = q[1] # q1' = q2
    q2 = a    # q2' = a
    return [q1, q2]
```
* This seems to be much faster than using `integrate.quad` somehow
  - `odeint`: 0.000112 s
  - `quad`: 0.001069 s

## Vertical acceleration
### How to find it
* I have vertical positions
  - The z position should be exact, if I do this right.
  - **THIS SHOULD BE A TEST**
* I have previous position and velocity
* `da/dt = (v-v0)/(dt)`
* `v0` is known
* `dt` is known
* I can find v (in z direction) from the two points and time step
  - Previous vertical position should be exact, so I can use that
  - Compare to something that's passed in
* One worry: this might be noisy comopared to the smoothing
  I can do with knowledge of the overall graph

#### Take 1

```python
def get_acceleration(self, current_z, initial_z, initial_vz, time_step):
    v = (current_z - initial_z) / time_step
    delta_v = v - initial_vz
    az = delta_v / time_step
    return az
```
* Thoughts on naming
  - Should I make this generic (ie, r and v?)
  - Physics notation? (z0 or initial_z)
  - delta_v and time_step are not consistent

### How to use it
```python
Ftz + Fg = m * az
Ftz = m * az  +  m * g
Ftz = m (a + g)

F * Fhat_z = m (a + g)
F = m (a + g) / Fhat_z

# Previously:
F = (m * g / Fhat_z)
```
