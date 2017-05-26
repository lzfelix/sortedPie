import bubble, bubble_improved, heap, insertion, merge, quick, select
import argparse
import random
import timeit
import os


def generate_array(range_size, mode, seed=42):
    if mode not in ['r', 'a', 'd']:
        raise ValueError('Mode should be (r)andom, (a)scending or (d)escending.')

    if mode == 'a':
        return list(range(range_size))

    elif mode == 'd':
        return list(range(range_size, -1, -1))

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
    elif algorithm_name == 'quick_left':
        algorithm = lambda x: quick.sort(x, False)
    elif algorithm_name == 'quick_median':
        algorithm = lambda x: quick.sort(x, True)
    elif algorithm_name == 'select':
        algorithm = select.sort
    else:
        raise ValueError('Invalid algorithm name')

    return algorithm


def generate_filename(algorithm, mode, n):
    if not os.path.isdir('reports'):
        os.mkdir('reports'.format(os.sep))

    return 'reports{}{}_{}_{}.csv'.format(os.sep, algorithm, mode, n)


def store_data_on_file(filename, execution_times):
    with open(filename, 'w') as f:
        s = ','.join([str(et) for et in execution_times])
        f.write(s)
        f.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser("Utility to benchmark sorting algorithms using Python's standard data structures")

    parser.add_argument('-a', help='The sorting algorithm to be used: bubble, bubble_improved, heap, insertion, ' +
                        'merge, quick_left, quick_median, select.', required=True, dest='algorithm')
    parser.add_argument('-m', help='How the generated numbers will be distributed: (a)scending, (d)escending,' +
                                   '(r)andom. Default is r.', default='r', type=str)
    parser.add_argument('-n', help='Amount of numbers to be generated for sorting. Default is 100.',
                        default=100, type=int)
    parser.add_argument('-t', help='Number of times that the benchmark will be repeated. Default is 10.',
                        default=10, type=int, dest='times')
    parser.add_argument('-f', help='If this flag is specified, this program will save the benchmark results on a .csv'
                        'file named [algorithm]_[mode]_[n].txt inside the reports/ folder. If such folder doesn\'t'
                        ' exist, it will be created.', action='store_true', dest='save_file')

    # extracting data from parser
    args = parser.parse_args()

    times = args.times
    mode = args.m.lower()
    algorithm_name = args.algorithm.lower()
    n = args.n

    # creating data to process
    algorithm = get_algorithm_by_name(algorithm_name)
    array = generate_array(n, mode)

    # running the benchmark
    execution_times = list()
    for i in range(times):
        print('Run {}/{}'.format(i+1, times), end='')
        execution_time = timeit.repeat(lambda: algorithm(array), number=1, repeat=1)
        print(' - {}'.format(execution_time[0]))

        execution_times.extend(execution_time)

    # calculating avg and standard deviation
    avg = sum(execution_times) / len(execution_times)

    sigma = 0
    for x in execution_times:
        sigma += (x-avg)**2
    sigma = (sigma / n) ** (1/2)

    print('Average: {}'.format(avg))
    print('std dev: {}'.format(sigma))

    # storing everything into a file
    if args.save_file:
        execution_times.extend([avg, sigma])
        filename = generate_filename(algorithm_name, mode, n)

        store_data_on_file(filename, execution_times)
