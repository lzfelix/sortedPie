from algorithms import bubble, bubble_improved, quick, select, insertion, heap, merge, quick_iterative
import random
import unittest


class Test(unittest.TestCase):
    ARRAY_SIZE = 200

    # If this value is set to None, the rand generator will use the current time as seed.
    # Use this for sorting different shuffled arrays on each test.
    RAND_GEN_SEED = 42

    def evaluate_algorithm(self, algorithm, range_size, mode, seed=RAND_GEN_SEED):
        if mode not in ['r', 'a', 'd']:
            raise ValueError('Mode should be (r)andom, (a)scending or (d)escending.')

        if mode == 'a':
            r = list(range(range_size))
            expected = r[:]
            assertion_message = "Test failed with array sorted in ascending order."

        elif mode == 'd':
            r = list(range(range_size, -1, -1))
            expected = sorted(r)
            assertion_message = "Test failed with array sorted in descending order."
        else:
            random.seed(seed)
            r = [random.randrange(2**15-1) for i in range(range_size)]
            expected = sorted(r)
            assertion_message = "Test failed with suffled array."

        self.assertEquals(expected, algorithm(r), assertion_message)

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
        self.run_all(bubble.sort, Test.ARRAY_SIZE)

    def test_bubble_sort_improved(self):
        self.run_all(bubble_improved.sort, Test.ARRAY_SIZE)

    def test_quicksort(self):
        self.run_all(quick.sort, Test.ARRAY_SIZE)

    def test_median_quicksort(self):
        median_quicksort = lambda x: quick.sort(x, use_median=True)
        self.run_all(median_quicksort, Test.ARRAY_SIZE)

    def test_selectsort(self):
        self.run_all(select.sort, Test.ARRAY_SIZE)

    def test_selectsort(self):
        self.run_all(insertion.sort, Test.ARRAY_SIZE)

    def test_heapsort(self):
        self.run_all(heap.sort, Test.ARRAY_SIZE)

    def test_mergesort(self):
        self.run_all(merge.sort, Test.ARRAY_SIZE)

    def test_iterative_quicksort(self):
        self.run_all(quick_iterative.sort, Test.ARRAY_SIZE)

    def test_iterative_median_quicksort(self):
        median_quicksort = lambda array: quick_iterative.sort(array, use_median=True)
        self.run_all(median_quicksort, Test.ARRAY_SIZE)

if __name__ == '__main__':
    unittest.main()
