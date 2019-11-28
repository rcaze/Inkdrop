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


def ink_drop(ndrops, ax=None, down=False, color=False, save=None):
    """Generate a drawing of diluted inkdrops"""
    if not ax:
        ax = plt.axes()
    adjust_spines(ax, ['']) #Remove the axis
    # Generate the random position of the drops
    xpos = random.rand(ndrops)
    ypos = random.rand(ndrops)
    op = np.linspace(0,1, ndrops)


    if down:
        xpos = np.concatenate((random.rand(ndrops//2),
                               random.rand(ndrops//4)*2,
                               random.rand(ndrops//4)*3))
        random.shuffle(op)


    if color:
        xpos = np.concatenate((random.rand(ndrops//3),
                               random.rand(ndrops//3)+1,
                               random.rand(ndrops//3)+2))
        color = [(random.rand(), 0, 0) for i in range(ndrops//3)]
        color += [(0, random.rand(), 0) for i in range(ndrops//3)]
        color += [(0, 0, random.rand()) for i in range(ndrops//3)]
        random.shuffle(op)
    else:
        color = ["black" for i in range(ndrops)]
    r = random.rand(ndrops)*0.04
    for i in range(ndrops):
        #color = (0, random.rand(), random.rand())
        #color = 'black'
        circle = plt.Circle((xpos[i], ypos[i]),
                            radius=r[i], fc=color[i],
                            alpha=op[i])
        ax.add_patch(circle)
    #ax.set_ylim(0,1)
    plt.axis('scaled') #To be sure to have a square
    if not save:
        plt.show()
        return
    else:
        plt.savefig(save, dpi=800)
        plt.close()
        return


if __name__ == "__main__":
    ndrops = 3000
    save = "inkdrop0.png"
    ink_drop(ndrops,save=save)
    save = "inkdropless.png"
    ink_drop(ndrops,save=save, down=True)
    save = "inkdroprgb.png"
    ink_drop(ndrops,save=save, color=True)

