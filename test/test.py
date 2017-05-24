from algorithms import bubble, bubble_improved, quick, select
import random
import unittest


class Test(unittest.TestCase):

    def evaluate_algorithm(self, algorithm, range_size, mode, seed=42):
        if mode not in ['r', 'a', 'd']:
            raise ValueError('Mode should be (r)andom, (a)scending or (d)escending.')

        if mode == 'a':
            r = list(range(range_size))
            expected = r
        elif mode == 'd':
            r = list(range(range_size, -1, -1))
            expected = sorted(r)
        else:
            random.seed(seed)
            r = [random.randrange(2**15-1) for i in range(range_size)]
            expected = sorted(r)

        self.assertEquals(expected, algorithm(r))

    def ascending(self, algorithm, range_size):
        self.evaluate_algorithm(algorithm, range_size, mode='a')

    def descending(self, algorithm, range_size):
        self.evaluate_algorithm(algorithm, range_size, mode='d')

    def random(self, algorithm, range_size, seed=42):
        self.evaluate_algorithm(algorithm, range_size, mode='r', seed=seed)

    def run_all(self, algorithm, size):
        self.ascending(algorithm, size)
        self.descending(algorithm, size)
        self.random(algorithm, size)

    def test_bubble_sort(self):
        self.run_all(bubble.sort, 100)

    def test_bubble_sort_improved(self):
        self.run_all(bubble_improved.sort, 100)

    def test_quicksort(self):
        self.run_all(quick.sort, 100)

    def test_median_quicksort(self):
        median_quicksort = lambda x: quick.sort(x, True)
        self.run_all(median_quicksort, 100)

    def test_selectsort(self):
        self.run_all(select.sort, 100)


if __name__ == '__main__':
    unittest.main()
