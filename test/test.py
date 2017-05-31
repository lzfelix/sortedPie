from algorithms import bubble, bubble_improved, quick, selection, insertion, heap, merge, quick_iterative
import random
import unittest


class Test(unittest.TestCase):
    ARRAY_SIZE = 500

    # If this value is set to None, the rand generator will use the current time as seed.
    # Use this for sorting different shuffled arrays on each test.
    RAND_GEN_SEED = 42

    def evaluate_algorithm(self, algorithm, range_size, mode, seed=RAND_GEN_SEED):
        """
        Tests if the sorting algorithm really works. If the array output by the algorithm is not sorted, an
        AssertionError is raised.
        :param algorithm: A Python function containing the algorithm to be tested.
        :param range_size: The size of the array used for testing
        :param mode: How the array is generated: on (a)scending order, (d)escending order, (r)andomized or (c)lustered.
         Each cluster is generated by sampling a 16-bit random unsigned int and has size range_size // 50.
        :param seed: The seed used to generate the random numbers.
        :return: None
        """

        if mode == 'a':
            r = list(range(range_size))
            assertion_message = "Test failed with array sorted in ascending order."

        elif mode == 'd':
            r = list(range(range_size-1, -1, -1))
            assertion_message = "Test failed with array sorted in descending order."

        elif mode == 'c':
            partition_size = range_size // 50
            assertion_message = 'Test failed with clustered array.'
            r = list()
            for i in range(range_size // partition_size):
                r.extend([random.randrange(2**16-1)] * partition_size)

        elif mode == 'r':
            random.seed(seed)
            r = [random.randrange(2**16-1) for i in range(range_size)]
            assertion_message = "Test failed with suffled array."

        else:
            raise ValueError('Mode should be (r)andom, (a)scending or (d)escending.')

        expected = sorted(r)
        self.assertEquals(expected, algorithm(r), assertion_message)

    def ascending(self, algorithm, range_size):
        self.evaluate_algorithm(algorithm, range_size, mode='a')

    def descending(self, algorithm, range_size):
        self.evaluate_algorithm(algorithm, range_size, mode='d')

    def random(self, algorithm, range_size, seed=42):
        self.evaluate_algorithm(algorithm, range_size, mode='r', seed=seed)

    def clustered(self, algorithm, range_size, seed=42):
        self.evaluate_algorithm(algorithm, range_size, mode='c', seed=seed)

    def run_all(self, algorithm, size):
        self.ascending(algorithm, size)
        self.descending(algorithm, size)
        self.random(algorithm, size)
        self.clustered(algorithm, size)

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
        self.run_all(selection.sort, Test.ARRAY_SIZE)

    def test_insertionsort(self):
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
