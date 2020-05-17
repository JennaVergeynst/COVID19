import numpy as np


def add_scalebar(ax, xy, length=50000., numdiv=5, fac="km", lw=5.,
                 marg=1000.):
    """
    Add a scalebar to the plot, using plot data units.

    Parameters
    -----------
    ax : mpl.axis
        current axis to scale bar
    xy : tuple of float
        x and y-coordinates of the lower left point of the scalebar, in map units
    lenght : float
        length in map units (m) of the scalebar
    numdiv : int
        number if division to split scalebar
    fac : str
        currently, only km for kilometer is supported
    lw : float
        width/length ratio
    marg : float
        distance between text and rectangles in map units
    """
    from itertools import cycle
    from matplotlib.patches import Rectangle

    # calculate left lower coordinates of rectangles
    x_pos = [xy[0] + i*length/numdiv for i in range(numdiv)]
    y = xy[1]
    # calculate labels
    dlabels = [int(i*length/numdiv/1000.) for i in range(numdiv + 1)]
    #put rectangles on the map
    for x, dlab, c in zip(x_pos, dlabels, cycle(['black', 'white'])):
        rect = Rectangle((x, y), length/numdiv,
                         length/numdiv/lw, facecolor=c, edgecolor='k',
                         zorder=10)
        ax.add_patch(rect)
        #ax.text(x_pos, y_pos + length/numdiv/lw + marg, dlab,
        #         horizontalalignment='center')
    #add last label
    #ax.text(ll_x_pos[-1] + length/numdiv, y_pos + length/numdiv/lw + marg,
    #         dlabels[-1], horizontalalignment='center')
    #put unit on it
#     if not fac=="km":
#         raise Exception('Only km as unit supported.')
#     else:
    ax.text(x_pos[-1] + length/numdiv + marg, y + length/numdiv/lw/2.,
                fac, horizontalalignment='left',
                verticalalignment='center', zorder=10)


def add_north_arrow(ax, xy, yheight=0.05, xwidth=0.04, marg=0.01):
    """
    Add a north arrow to the plot, using relative Axes units

    Parameters
    -----------
    ax : mpl.axis
        current axis to add north arrow
    xy : tuple of 2 floats
        x and y-coordinates of the top point of the north arrow, in relative axes units
    yheigth : float
        distance in map units between the top point and the moddle point of
        the arrow
    xwidth : float
        width of the arrow in map units
    marg : float
        distance between text and rectangles in map units
    """
    from matplotlib.patches import Polygon

    x_a, y_a = xy

    #add north arrow
    ylow = np.sqrt(yheight**2 - xwidth**2)

    #triangles to make north arrow
    rpol = Polygon(np.array([[x_a, y_a] ,[x_a, y_a - yheight],
                   [x_a + xwidth/2., y_a - yheight - ylow]]),
                   facecolor='w', edgecolor='k', transform=ax.transAxes,
                   zorder=10)
    ax.add_patch(rpol)
    lpol = Polygon(np.array([[x_a, y_a] ,[x_a, y_a - yheight],
                   [x_a - xwidth/2., y_a - yheight - ylow]]),
                   facecolor='k', edgecolor='k', transform=ax.transAxes,
                   zorder=10)
    ax.add_patch(lpol)

    # N text
    ax.text(x_a, y_a + marg, "N", horizontalalignment='center',
            transform=ax.transAxes, zorder=10)


