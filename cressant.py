# A Dodecahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin, tan, log1p
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

def x_(u,v):
	x = (2 + sin(2 * pi * v) * sin(2 * pi * u)) * sin(3 * pi * v)
	return x

def y_(u,v):
	y = sin(2 * pi * v) * cos(2 * pi * u) + 4 * v - 2
	return y

def z_(u,v):
	z = (2 + sin(2 * pi * v) * sin(2 * pi * u)) * cos(3 * pi * v)
	return z

u = linspace(0, 1, 50)
v = linspace(0, 1, 50)

u, v = np.meshgrid(u, v)

x = x_(u,v)
y = y_(u,v)
z = z_(u,v)

# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')

#ax.set_xlim(-1,1)
#ax.set_ylim(-1,1)
#ax.set_zlim(-10,10)

# Surface Plot
ho = ax.plot_surface(x, y, z)

ho.set_alpha(1)
ho.set_edgecolor('w')
ho.set_linewidth(0.5)
ho.set_facecolor('deepskyblue')

# Definitions for animation
def init():
	return ho,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

   		ax.view_init(elev=29, azim=90)
		return ho,
# 29
# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                   frames=100, interval=1, blit=False, repeat=True)

# Saving to Cross-Cap.mp4

#Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('Cross-Cap.mp4', writer=writer)

plt.show()
