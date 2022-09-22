"""Numpy-compatible routines for a standard cycloid (one caused by a
circle of radius r above the y-axis rolling along the positive x-axis
starting from the origin).
"""
import numpy as np

def x(t, r):
    """Return the x-coordinate of a point on the cycloid with parameter t."""
    return r * (t - np.sin(t))

def y(t, r):
    """Return the y-coordinate of a point on the cycloid with parameter t."""
    return r * (1.0 - np.cos(t))

def dir_angle_norm_in(t, r):
    """Return the direction angle of the vector normal to the cycloid at
    the point with parameter t that points into the cycloid."""
    return -t / 2.0

def dir_angle_norm_out(t, r):
    """Return the direction angle of the vector normal to the cycloid at
    the point with parameter t that points out of the cycloid."""
    return np.pi - t / 2.0

def arclen(t, r):
    """Return the arc length of the cycloid between the origin and the
    point on the cycloid with parameter t."""
    return 4.0 * r * (1.0 - np.cos(t / 2.0))


# Roulette problem

def xy_roulette(t, r, T, R):
    """Return the x-y coordinates of a rim point on a circle of radius
    R  rolling on a cycloid of radius r starting at the anchor point
    with parameter T currently at the point with parameter t. (Such a
    rolling curve on another curve is called a roulette.)
    """
    # Find the coordinates of the contact point P between circle and cycloid
    px, py = x(t, r), y(t, r)
    # Find the direction angle of PC from the contact point to circle's center
    a1 = dir_angle_norm_out(t, r)
    # Find the coordinates of the center C of the circle
    cx, cy = px + R * np.cos(a1), py + R * np.sin(a1)
    # Find cycloid's arc distance AP between anchor and current contact points
    d = arclen(t, r) - arclen(T, r)  # equals arc PF
    # Find the angle φ the circle turned while rolling from the anchor pt
    phi = d / R
    # Find the direction angle of CF from circle's center to rim point
    a2 = dir_angle_norm_in(t, r) - phi  # subtract: circle rolls clockwise
    # Find the coordinates of the final point F
    fx, fy = cx + R * np.cos(a2), cy + R * np.sin(a2)
    # Return those coordinates
    return fx, fy

import matplotlib.pyplot as plt

r = 1
R = 0.75
T = np.pi / 3

t_array = np.linspace(0, 2*np.pi, 601)
cycloid_x = x(t_array, r)
cycloid_y = y(t_array, r)
# roulette_x, roulette_y = xy_roulette(t_array, r, T, R)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

ax.plot(cycloid_x, cycloid_y)
# ax.plot(roulette_x, roulette_y)

plt.show()