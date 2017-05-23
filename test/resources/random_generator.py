import argparse
import random


def list_to_str(l):
    return ' '.join(map(str, l))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Generates n random numbers')
    parser.add_argument('-n', help='Amount of numbers to be generated. Default is 100.', default=100, type=int)
    parser.add_argument('-m', help='Mode: (a)scending, (d)escending, (r)andom. Default is r.', default='r', type=str)
    parser.add_argument('-f', help='Saves the generated list as a file named [mode]_[n].txt.', action='store_true')

    args = parser.parse_args()
    mode = args.m.lower()
    n    = args.n

    if mode not in ['r', 'a', 'd']:
        raise ValueError('-r should be either r, a or d.')

    output = None

    if mode == 'a':
        output = list_to_str(range(n))

    elif mode == 'd':
        output = list_to_str(range(n, -1, -1))

    else:
        x = [random.randrange(0, 2**15-1) for i in range(n)]
        output = list_to_str(x)

    if not args.f:
        print(output)
    else:
        mode_names = {'r': 'random', 'a': 'ascending', 'd': 'descending'}
        filename = mode_names[mode] + '_' + str(n) + '.txt'

        with open(filename, 'w') as file:
            file.write(output)
