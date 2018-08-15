# A Hyperbolic Octahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers


def x_(u,v):
	x = (cos(u) * cos(v)) * (cos(u) * cos(v)) * (cos(u) * cos(v))
	return x

def y_(u,v):
	y = (sin(u) * cos(v)) * (sin(u) * cos(v)) * (sin(u) * cos(v))
	return y

def z_(u,v):
	z = sin(v) * sin(v) * sin(v)
	return z

u = linspace(-pi/2, pi/2, 25)
v = linspace(-pi, pi, 25)

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

ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-1,1)

# Surface Plot
ho = ax.plot_surface(x, y, z)

ho.set_alpha(1)
ho.set_edgecolor('w')
ho.set_linewidth(1)
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
    # Optimal Viewing angle: elev = 29

   		ax.view_init(elev=i, azim=i*4)
		return ho,
	
# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                   frames=100, interval=20, blit=False, repeat=True)

# Saving to Hyperbolic-Octahedron.mp4

#Writer = writers['ffmpeg']
#writer = Writer(fps=15, bitrate=1800)

#ani.save('Hyperbolic-Octohedron.mp4', writer=writer)

plt.show()