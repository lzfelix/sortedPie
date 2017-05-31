from algorithms import bubble, bubble_improved, heap, insertion, merge, quick, selection, quick_iterative
import argparse
import random
import timeit
import os


def generate_array(range_size, mode, seed=None):
    """Generates a sorted [0..n-1], reversed-sorted [n-1..0] or shuffled array according to mode. Seed is only used
    on the latter case."""

    if mode not in ['r', 'a', 'd']:
        raise ValueError('Mode should be (r)andom, (a)scending or (d)escending.')

    if mode == 'a':
        return list(range(range_size))

    elif mode == 'd':
        return list(range(range_size-1, -1, -1))

    else:
        random.seed(seed)
        return [random.randrange(2 ** 15 - 1) for i in range(range_size)]


def get_algorithm_by_name(algorithm_name):

    if algorithm_name == 'bubble':
        algorithm = bubble.sort
    elif algorithm_name == 'bubble_improved':
        algorithm = bubble_improved.sort
    elif algorithm_name == 'heap':
        algorithm = heap.sort
    elif algorithm_name == 'insertion':
        algorithm = insertion.sort
    elif algorithm_name == 'merge':
        algorithm = merge.sort
    elif algorithm_name == 'quick':
        algorithm = lambda array: quick.sort(array, False)
    elif algorithm_name == 'quick_median':
        algorithm = lambda array: quick.sort(array, True)
    elif algorithm_name == 'selection':
        algorithm = selection.sort
    elif algorithm_name == 'iquick':
        algorithm = lambda array: quick_iterative.sort(array, False)
    elif algorithm_name == 'iquick_median':
        algorithm = lambda array: quick_iterative.sort(array, True)
    else:
        raise ValueError('Invalid algorithm name')

    return algorithm


def generate_filename(algorithm, mode, n):
    current_dir = os.getcwd()
    reports_folder = os.path.join(current_dir, 'reports')

    if not os.path.isdir(reports_folder):
        os.mkdir(reports_folder)

    filename = '{}_{}_{}.csv'.format(algorithm, mode, n)
    return os.path.join(reports_folder, filename)


def store_data_on_file(filename, execution_times):
    with open(filename, 'w') as f:
        s = ','.join([str(et) for et in execution_times])
        f.write(s)
        f.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser("Utility to benchmark sorting algorithms using Python's standard data structures",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a', help='The sorting algorithm to be used: bubble, bubble_improved, heap, insertion, ' +
                        'merge, quick, quick_median, selection, iquick, iquick_median.', required=True,
                        dest='algorithm', default=argparse.SUPPRESS)
    parser.add_argument('--mode', help='How the generated numbers will be distributed: (a)scending, (d)escending,' +
                                   '(r)andom.', default='r', type=str)
    parser.add_argument('--size', help='Amount of numbers to be generated for sorting.', default=100, type=int)
    parser.add_argument('--times', help='Number of times that the benchmark will be repeated.', default=10, type=int,
                        dest='times')
    parser.add_argument('-f', help='If this flag is specified, this program will save the benchmark results on a .csv'
                        'file named [algorithm]_[mode]_[n].txt inside the reports/ folder. If such folder doesn\'t'
                        ' exist, it will be created in the same directory where this script was invoked. The .csv '
                        'format is time_run1,time_run2,...time_runN,average,standard_deviation.', action='store_true',
                        dest='save_file')

    # extracting data from parser
    args = parser.parse_args()

    times = args.times
    mode = args.mode.lower()
    algorithm_name = args.algorithm.lower()
    n = args.size

    # picking the algorithm
    algorithm = get_algorithm_by_name(algorithm_name)

    # running the benchmark
    execution_times = list()
    for i in range(times):
        print('Run {}/{}'.format(i+1, times), end='')
        array = generate_array(n, mode)
        execution_time = timeit.repeat(lambda: algorithm(array), number=1, repeat=1)
        print(' - {}'.format(execution_time[0]))

        execution_times.extend(execution_time)

    # calculating avg and standard deviation
    avg = sum(execution_times) / len(execution_times)

    sigma = 0
    for x in execution_times:
        sigma += (x-avg)**2
    sigma = (sigma / (n - 1)) ** (1/2)

    avg = sum(execution_times) / len(execution_times)

    sigma = 0
    for x in execution_times:
        sigma += (x - avg) ** 2
    sigma = (sigma / n) ** (1 / 2)

    print('Average: {}'.format(avg))
    print('std dev: {}'.format(sigma))

    # storing everything into a file
    if args.save_file:
        execution_times.extend([avg, sigma])
        filename = generate_filename(algorithm_name, mode, n)

        store_data_on_file(filename, execution_times)
