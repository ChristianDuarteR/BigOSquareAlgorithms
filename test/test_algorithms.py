import unittest
from python import algorithms

arrays = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [2], [2, 1], [1, 2], [2, 4, 6], [1, 3, 9], [10, 8], [11, 31]]
expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [2], [1, 2], [1, 2], [2, 4, 6], [1, 3, 9], [8, 10], [11, 31]]

sequences = [("AGGTAB", "GXTXAYB"), ("ABCBDAB", "BDCAB"), ("XMJYAUZ", "MZJAWXU")]
expected_seq = [4, 4, 4]




class AlgorithmsTests(unittest.TestCase):
    def test_bubble_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            exp = expected[i]
            algorithms.improved_bubble_sort(array)
            self.assertEquals(array, exp)

    def test_shell_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            exp = expected[i]
            algorithms.shell_sort(array)
            self.assertEquals(array, exp)

    def test_longest_subsequence(self):
        for i in range(len(sequences)):
            sequence = sequences[i]
            exp = expected_seq[i]
            answer = algorithms.longest_common_subsequence(sequence)
            self.assertEqual(exp, answer)


if __name__ == "__main__":
    unittest.main()
