import numpy as np
import matplotlib.pyplot as plt


# Simple line plot
def line():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()


# Graph by Point
def point():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # ro (red circle)
    plt.axis([0, 6, 0, 20])  # axis (Length axis to x and y directions [xmin, xmax, ymin, ymax])
    plt.show()


# using numpy with matplotlib
def multiple_graph():
    t = np.arange(0., 5., 0.2)  # numpy array
    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
    plt.xlabel('t')
    plt.show()


# function to be plotted
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


# plotting many figures
def multiple_figure():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure()
    plt.subplot(211)  # numrows, numcols, plot_number
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
    plt.show()


# annotation on graph
def annoting():
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05),)
    plt.ylim(-2, 2)
    plt.show()


# text on graph
def text():
    fig = plt.figure()
    fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_title('axes title')

    ax.set_xlabel('xlabel')
    ax.set_ylabel('ylabel')

    ax.text(3, 8, 'boxed italics text in data coords', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

    ax.text(3, 2, u'unicode: Institut f\374r Festk\366rperphysik')

    ax.text(0.95, 0.01, 'colored text in axes coords',
            verticalalignment='bottom', horizontalalignment='right',
            transform=ax.transAxes,
            color='green', fontsize=15)

    ax.plot([2], [1], 'o')
    ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
                arrowprops=dict(facecolor='black', shrink=0.05))

    ax.axis([0, 10, 0, 10])

    plt.show()


# Math text on graph
def math_text():
    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(2 * np.pi * t)

    plt.plot(t, s)
    plt.title(r'$\alpha_i > \beta_i$', fontsize=20)
    plt.text(1, -0.6, r'$\sum_{i=0}^\infty x_i$', fontsize=20)
    plt.text(0.6, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$', fontsize=20)
    plt.xlabel('time (s)')
    plt.ylabel('volts (mV)')
    plt.show()


# legend adding on figure
def legend_graph():
    line1, = plt.plot([1, 2, 3], label="Line 1", linestyle='--')
    line2, = plt.plot([3, 2, 1], label="Line 2", linewidth=4)

    # Create a legend for the first line.
    first_legend = plt.legend(handles=[line1], loc=1)

    # Add the legend manually to the current Axes.
    ax = plt.gca().add_artist(first_legend)

    # Create another legend for the second line.
    plt.legend(handles=[line2], loc=4)

    plt.show()


if __name__ == '__main__':
    # line()
    # point()
    # multiple_graph()
    # multiple_figure()
    # annoting()
    # text()
    # math_text()
    legend_graph()
