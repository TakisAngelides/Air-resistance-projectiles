from numpy import cos, sin, pi, sqrt, average
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('dark_background')

# We need to specify x0, y0, vx0, vy0, keep track of x, y, vx, vy and return x, y

dt = 0.0001 # time step

steps = 50000 # number of steps to perform

g = 9.8 # gravitational strength

k = 1 # strength of drag

m = 1 # mass

n = 1 # power law of drag with speed

v0 = 10 # initial speed

angle0 = 30 # initial angle with respect to the x-axis

x0, y0, vx0, vy0 = 0, 0, v0*cos(angle0*pi/180), v0*sin(angle0*pi/180) # in the cos and sin functions we pass radians = angle in degrees * pi / 180

x, y, vx, vy = [x0], [y0], [vx0], [vy0]

def integrate():

    for i in range(steps):

        x.append(x[i] + vx[i] * dt) # x_new = x_old + v_x * dt

        y_new = y[i] + vy[i] * dt # y_new = y_old + v_y * dt

        y.append(y_new)

        speed = sqrt(vx[i]**2 + vy[i]**2) # speed = sqrt(v_x**2 + v_y**2) = |v|

        vx.append(vx[i] + (1/m) * dt * (-k * (speed**n) * vx[i]/speed)) # v_x_new = v_x + (1/m) * dt * F_x which implies F_x = -k * (|v|**n) * vx[i]/|v|)

        vy_new = vy[i] + (1/m) * dt * (-k * (speed**n) * vy[i]/speed - g) # v_x_new = v_x + (1/m) * dt * F_y which implies F_y = -k * (|v|**n) * vy[i]/|v| - g

        if (y[i] > 0) and (y_new < 0): # if y position was positive in the previous time step and negative in this time step then reverse the y velocity

            vy.append(-vy_new) # make the bounce on the ground at y = 0

        else:

            vy.append(vy_new)

    return x, y

pos_x, pos_y = integrate()


fig = plt.figure()
ax = plt.axes(xlim=(-0, 10), ylim=(0, 1))
plt.xticks([])
plt.yticks([])
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

x_list, y_list = [], []

def animate(i):

    if i*40 > len(x)-1:
        pass
    else:
        x_list.append(x[i*40])
        y_list.append(y[i*40])
        line.set_data(x_list, y_list)
    return line,

anim = FuncAnimation(fig, animate, init_func=init, interval = 0.0000000001, repeat = False)
plt.show()

plt.plot(pos_x, pos_y)
plt.title(f'k = {k}, g = {g}, m = {m}, n = {n}, v0 = {v0}, angle0 = {angle0}')
plt.show()
