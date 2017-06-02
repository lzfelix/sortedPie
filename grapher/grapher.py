import os
import os.path as osp

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator


def generate_filename(algorithm_name):
    """Generates the base name of the file containing a given graph. The files are saved on the graphs/ folder having
    with the algorithm name."""

    graphs_dir = osp.join(os.getcwd(), 'graphs')
    if not os.path.isdir(graphs_dir):
        os.mkdir(graphs_dir)

    return osp.join(graphs_dir, algorithm_name)


def setup_mpl():
    """Setup of font and draw area sizes."""
    mpl.rcParams['font.size'] = 15
    mpl.rcParams['axes.labelsize'] = 15
    mpl.rcParams['axes.labelpad'] = 10

    plt.gcf().set_size_inches(7.2, 7.2)


def post_plotting_design():
    """Adds legends, pads axes label, soften grid color."""

    leg = plt.legend(fancybox=True, title=r'$\bf{Array}$')

    # set the linewidth of each legend object
    for legobj in leg.legendHandles:
        legobj.set_linewidth(2.0)

    # Forcing matplotlib to start the axes at (0,0)
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)

    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo (s)')

    # Making x-grid [10000,20000,...]
    plt.axes().xaxis.set_major_locator(MultipleLocator(10000))
    plt.axes().xaxis.set_minor_locator(MultipleLocator(5000))

    plt.grid(True, color=(0.9, 0.9, 0.9))
    plt.grid(True, which='minor', color=(0.9, 0.9, 0.9))


def plot(name, stats):
    """Given the statistics dict generated by the assemble_data code, plots a graph (input_size vs execution_time) and
    saves it as graphs/algorithm_name.{eps,png}."""
    # by the project design, all executions are under the same dataset, so fetching from a single one should be fine.
    x = stats['r']['size']

    # getting the execution times.
    y_random = stats['r']['average_time'] if 'r' in stats else []
    y_asc = stats['a']['average_time'] if 'a' in stats else []
    y_desc = stats['d']['average_time'] if 'd' in stats else []

    setup_mpl()

    plt.plot(x, y_random, label='Embaralhado', color='#279427')
    if y_asc:
        plt.plot(x, y_asc, label='Crescente', linewidth=3, color='#1C6CAA')
        # plt.plot(x, y_asc, label='Crescente', color='#1C6CAA')

    if y_desc:
        plt.plot(x, y_desc, label='Decrescente', color='#FF7311')

    post_plotting_design()

    fig = plt.gcf()

    filename = generate_filename(name)
    fig.savefig('{}.eps'.format(filename), format='eps', dpi=1000)
    fig.savefig('{}.png'.format(filename), format='png')
    fig.clear()