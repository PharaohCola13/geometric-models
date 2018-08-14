# A Cube, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import pi, linspace, cos, sin
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

points = np.array([[-1, -1, -1],
                  [1, -1, -1 ],
                  [1, 1, -1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [1, -1, 1 ],
                  [1, 1, 1],
                  [-1, 1, 1]])

# Scaling Matricies
P = [[2, 0, 0],
	 [0, 2, 0],
	 [0, 0, 2]]


Z = np.zeros((8,3))


for i in range(8): 
	Z[i,:] = np.dot(points[i,:],P)

# Figure Properties
fig = plt.figure(figsize=(8,8))

ax = p3.Axes3D(fig)
ax.set_facecolor('black')

plt.axis('off')
plt.axis('equal')

ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_zlim(-4,4)

# Interval
r = [-1,1]

X, Y = np.meshgrid(r, r)

# Side Configuration for Cube
verts_cube = [[Z[0],Z[1],Z[2],Z[3]],
	[Z[4],Z[5],Z[6],Z[7]], 
	[Z[0],Z[1],Z[5],Z[4]], 
	[Z[2],Z[3],Z[7],Z[6]], 
	[Z[1],Z[2],Z[6],Z[5]],
	[Z[4],Z[7],Z[3],Z[0]], 
	[Z[2],Z[3],Z[7],Z[6]]]


# Cube Properties
cube = Poly3DCollection(verts_cube)

cube.set_edgecolor('white')
cube.set_linewidth(1)
cube.set_alpha(0.1)
cube.set_facecolor('blue')

# Plot Surfaces
ax.add_collection3d(cube)


# Defintions for animations
def init():
    return cube,

def animate(i):
    # azimuth angle : 0 deg to 360 deg
    # elev = i * n --> rotates object about the xy-plane with a magnitude of n
    # azim = i * n --> rotates object around the z axis with a magnitude of n
    # For top view elev = 90
    # For side view elev = 0

    ax.view_init(elev=0, azim= 4 * i)
    return cube,

# Animate
ani = FuncAnimation(fig, animate, init_func=init,
                  frames=110, interval=1, blit=False, repeat=True)

# Saving to Cube.mp4

# Writer = writers['ffmpeg']
# writer = Writer(fps=15, bitrate=1800)

# ani.save('Cube.mp4', writer=writer)


plt.show()