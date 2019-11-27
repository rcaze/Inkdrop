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


fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(0,1), ylim=(0,1))
adjust_spines(ax, ['']) #Remove the axis

def init(maxt = 1000):
    # Generate the random position of the drops
    xpos = random.rand(maxt)
    ypos = random.rand(maxt)
    color = [(0, random.rand(), 0) for i in range(maxt)]
    return xpos, ypos, color

tmax=25000
xpos, ypos, color = init(tmax)

def ink_rain(t, drop_life=30):
    """Generate a drawing of diluted inkdrops"""
    plt.cla()
    adjust_spines(ax, ['']) #Remove the axis
    opacity = np.linspace(1, 0, drop_life)
    radius = np.linspace(0.035, 0.2, drop_life)
    j = 0
    for i in range(t, max(0, t-drop_life), -1):
        circle = plt.Circle((xpos[i], ypos[i]),
                            radius=radius[j],
                            fc=color[i],
                            alpha=opacity[j])
        j += 1
        ax.add_patch(circle)
    return ax

if __name__ == "__main__":
    anim = FuncAnimation(fig, ink_rain, init_func=init,
                         frames=tmax, interval=50)
    anim.save('ink_rain.avi')
    #plt.show()

