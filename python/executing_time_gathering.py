import time

from python import algorithms
from python import constants
from python import data_generator


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = []
    samples_seq = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))
        samples_seq.append(data_generator.get_random_seq(size))
    return [
        take_time_for_algorithm(samples, algorithms.improved_bubble_sort),
        take_time_for_algorithm(samples, algorithms.shell_sort),
        take_time_for_algorithm(samples_seq, algorithms.longest_common_subsequence),
    ]

"""
    Returns the median of the execution time measures for a sorting approach given in 
"""

def take_time_for_algorithm(samples_array, sorting_approach):
    times = []

    for sample in samples_array:
        start_time = time.time()
        if isinstance(sample[0], int):
            sorting_approach(sample.copy())
        else:
            sorting_approach(sample)
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))
    # Tomar mediana
    times.sort()
    return times[len(times) // 2]
