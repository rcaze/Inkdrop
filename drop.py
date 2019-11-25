from numpy import random
import numpy as np
import matplotlib.pyplot as plt

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


def ink_drop(ndrops, ax=None, save=None):
    """Generate a drawing of diluted inkdrops"""
    if not ax:
        ax = plt.axes()
    adjust_spines(ax, ['']) #Remove the axis
    # Generate the random position of the drops
    xpos = random.rand(ndrops)
    ypos = random.rand(ndrops)
    # Set the linearly deacrising opacity of drops
    op = np.linspace(0,1, ndrops)
    for i in range(ndrops):
        circle = plt.Circle((xpos[i], ypos[i]),
                            radius=0.025, fc='black',
                            alpha=op[i])
        ax.add_patch(circle)

    plt.axis('scaled') #To be sure to have a square
    if not save:
        plt.show()
        return
    else:
        plt.savefig(save, dpi=800)
        plt.close()
        return

if __name__ == "__main__":
    ndrops = 1000
    save = "InkDrop0.png"
    ink_drop(ndrops,save=save)
