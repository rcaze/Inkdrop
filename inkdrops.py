from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def adjust_spines(ax, spines):
    """
    removing the spines from a matplotlib graphics.
    taken from matplotlib gallery anonymous author.

    parameters
    ----------
    ax: a matplolib axes object
        handler of the object to work with
    spines: list of char
        location of the spines

    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            pass
            # print 'skipped'
            # spine.set_position(('outward',10)) # outward by 10 points
            # spine.set_smart_bounds(true)
        else:
            spine.set_color('none')
            # don't draw spine
            # turn off ticks where there is no spine

    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        # no yaxis ticks
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        # no xaxis ticks
        ax.xaxis.set_ticks([])


rmax = 0.2
colored = False

if colored:
    fig = plt.figure(figsize=(15,5))
    ax = plt.axes(xlim=(0-rmax,1+rmax), ylim=(0-rmax,1+rmax))
    adjust_spines(ax, ['']) #Remove the axis
else:
    fig = plt.figure(figsize=(5, 5))
    ax = plt.axes(xlim=(0-rmax,1+rmax), ylim=(0-rmax,3+rmax))
    adjust_spines(ax, ['']) #Remove the axis


tmax= 300 #If colored is true need to be possible to divide by 3
ndrops = 10
drop_life = 50
rmax = 0.4
# Need to define the position of all drops
# Their opacity at a given time and the related diameter
def init():
    # Generate the random position of the drops
    fall = np.zeros((ndrops, 4, tmax))
    for i in range(ndrops):
        fall_t = np.random.randint(tmax)
        coor = np.random.rand(2)
        k = 0
        radius = np.linspace(0.05, rmax, drop_life)
        opacity = np.linspace(1, 0, drop_life)
        for j in range(fall_t, min(fall_t + drop_life, tmax)):
            fall[i,0,j] = opacity[k]
            fall[i,1,j] = radius[k]
            fall[i,2,j] = coor[0]
            fall[i,3,j] = coor[1]
            k +=1
    return fall

fall = init()

def ink_rain(t):
    """Generate a drawing of diluted inkdrops"""
    plt.cla()
    adjust_spines(ax, ['']) #Remove the axis
    ax.set_xlim(0-rmax, 1+rmax)
    ax.set_ylim(0-rmax, 1+rmax)
    for i in range(ndrops):
        if fall[i,0,t] > 0.1:
            circle = plt.Circle((fall[i, 2, t], fall[i, 3, t]),
                                radius=fall[i, 1,t],
                                fc="black",
                                alpha=fall[i, 0,t])
            ax.add_patch(circle)
    return ax

if __name__ == "__main__":
    anim = FuncAnimation(fig, ink_rain, init_func=init,
                         frames=tmax, interval=20)
    anim.save('Rainy_sunday.avi')
    #anim.save('spreading_ink.avi')
    plt.show()

