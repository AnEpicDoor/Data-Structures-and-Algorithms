import math
import random
import matplotlib.pyplot as plt
import statistics

# random array used for testing
random_test_array = []

# number of elements to be added to random array
for i in range(1024):
    # elements are integers between 10*cardinality and 100*cardinality
    random_test_array.append(random.randint(10*1024, 100*1024))

# arrays used for testing whether the algorithms function as expected
test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
test2 = [53, 23, 73, 36, 82, 70, 26, 92, 98, 88, 79, 48, 16, 14, 49, 23]
test_walkthrough = [1, 3, 8, 4, 5, 7, 2, 6]


# algorithm a
def algorithm_a(array):

    # find middle index of array
    middle = len(array) // 2

    # add first half of array to S1, add second half to S2
    s1 = array[:middle]
    s2 = array[middle:]

    # return subsets
    return s1, s2


# algorithm b
def algorithm_b(array):

    # initialise empty subsets
    s1 = []
    s2 = []

    # loop through array
    for i in range(len(array)):

        if i % 2 == 0:
            # append even-indexed element to subset 1
            s1.append(array[i])
        else:
            # append odd-indexed element to subset 2
            s2.append(array[i])

    # return subsets
    return s1, s2


# algorithm c
def algorithm_c(array):

    # initialise empty subsets
    s1 = []
    s2 = []

    # loop through array
    for x in array:

        if x % 2 == 0:
            # if element is even then append to subset 1
            s1.append(x)
        else:
            # else append to subset 2
            s2.append(x)

    # return subsets
    return s1, s2


# algorithm d
def algorithm_d(array):

    # initialise empty subsets
    s1 = []
    s2 = []

    # append first element to subset 1, append second element to subset 2
    s1.append(array[0])
    s2.append(array[1])

    # loop through the rest of the elements
    for i in range(2, len(array)):

        if sum(s1) <= sum(s2):
            # if sum of subset 1 is less than or equal to subset 2 then append to subset 1
            s1.append(array[i])
        else:
            # else append to subset 2
            s2.append(array[i])

    # return subsets
    return s1, s2


# algorithm e
def algorithm_e(array):

    # initialise empty subsets
    s1 = []
    s2 = []

    # sort array into ascending order
    array.sort()

    # loop through elements
    for i in range(len(array)):
        if i % 2 == 0:
            # append even-indexed element to the even array
            s1.append(array[i])
        else:
            # append odd-indexed element to the odd array
            s2.append(array[i])

    # return subsets
    return s1, s2


# algorithm f
def algorithm_f(array):

    # initialise empty subsets
    s1 = []
    s2 = []

    # sort array into ascending order
    array.sort()

    # append first element to subset 1, append second element to subset 2
    s1.append(array[0])
    s2.append(array[1])

    # loop through the rest of the elements
    for i in range(2, len(array)):
        if sum(s1) <= sum(s2):
            # if subset 1 is smaller or equal to subset 2, append to subset 1
            s1.append(array[i])
        else:
            # else append to subset 2
            s2.append(array[i])

    # return subsets
    return s1, s2


# algorithm g
def algorithm_g(array):

    # initialise empty subsets
    s1 = []
    s2 = []

    # sort array in descending order
    array.sort(reverse=True)

    # append first element to subset 1, append second element to  subset 2
    s1.append(array[0])
    s2.append(array[1])

    # loop through the rest of the elements
    for i in range(2, len(array)):
        if sum(s1) <= sum(s2):
            # if subset 1 is smaller or equal to subset 2 then append to subset 1
            s1.append(array[i])
        else:
            # else append to subset 2
            s2.append(array[i])

    # return subsets
    return s1, s2


# algorithm h
def algorithm_h(array):

    # n = length of array
    n = len(array)

    # initialise minimum difference to infinity
    min_diff = float('inf')

    # initialise variables to store subsets with minimum difference
    min_s1 = []
    min_s2 = []

    # iterate through all 2-way partitions of array
    for i in range(n):
        for j in range(i + 1, n):

            # subset 1 is the slice of the array from index i to index j
            s1 = array[i:j]

            # subset 2 contains all the elements not in s1
            s2 = [x for x in array if x not in s1]

            # find absolute difference between subset 1 and subset 2
            diff = abs(sum(s1) - sum(s2))

            # update minimum difference and smallest partition if necessary
            if diff < min_diff:
                min_diff = diff
                min_s1 = s1
                min_s2 = s2

    # return the ideal subsets
    return min_s1, min_s2


# algorithm i
def algorithm_i(array):

    # find ideal sum
    ideal_sum = sum(array)/2

    # sort it in descending order
    sorted_array = sorted(array, reverse=True)

    # initialise subsets
    s1 = []
    s2 = []

    # loop through array
    while sorted_array:
        if sum(s1) <= sum(s2):
            # if s1 has a smaller or equal sum to s2 then append element to s1
            s1.append(sorted_array.pop(0))
        else:
            # otherwise append to s2
            s2.append(sorted_array.pop(0))

    # if subsets are equal return subsets
    if sum(s1) == sum(s2):
        return s1, s2

    # if s1 is greater than s2 then swap them, this is done so that when swapping individual elements in the next step
    # the sum of the set with the already larger sum isn't increased
    if sum(s1) > sum(s2):
        s1, s2 = s2, s1

    # loop through elements in both subsets
    for i in s1:
        for j in s2:

            # keep track of sums in s1 and s2 if elements were to be swapped
            temp_sum_s1 = sum(s1) - i + j
            temp_sum_s2 = sum(s2) - j + i

            # if temporary sum of s1 is closer to the ideal sum than sum of s1
            # and temporary sum of s2 is closer to the ideal sum than sum of s2
            if abs(temp_sum_s1 - ideal_sum) < abs(sum(s1) - ideal_sum) \
                    and abs(temp_sum_s2 - ideal_sum) < abs(sum(s2) - ideal_sum):

                # create new subsets with swapped elements
                # new subsets are created to avoid an error that sometimes happens
                # if the elements are appended to the original s1 and s2
                s1 = [j if x == i else x for x in s1]
                s2 = [i if x == j else x for x in s2]

    # return subsets
    return s1, s2


# list of algorithms (test harness takes list of algorithm as input)
list_algorithms = [algorithm_a, algorithm_b, algorithm_c, algorithm_d, algorithm_e, algorithm_f, algorithm_g,
                   algorithm_h, algorithm_i]

# list of mean deviations (used to store output from test harness)
list_mean_deviations_a = []
list_mean_deviations_b = []
list_mean_deviations_c = []
list_mean_deviations_d = []
list_mean_deviations_e = []
list_mean_deviations_f = []
list_mean_deviations_g = []
list_mean_deviations_h = []
list_mean_deviations_i = []

# list of standard deviations (used to store output from test harness)
list_standard_deviations_a = []
list_standard_deviations_b = []
list_standard_deviations_c = []
list_standard_deviations_d = []
list_standard_deviations_e = []
list_standard_deviations_f = []
list_standard_deviations_g = []
list_standard_deviations_h = []
list_standard_deviations_i = []


# test harness for algorithms, takes a list of algorithms as input, runs each algorithm 1000 times for each cardinality
# stores mean deviation from the ideal subset sum and standard deviation of mean deviations from ideal subset sum
def test_harness(algorithm_list):

    # loop through all algorithms in list
    for algorithm in algorithm_list:

        # calculate cardinality, run algorithms for each cardinality
        for i in range(0, 8):

            # temporarily stores mean deviations for each run through the algorithm
            temp_list_deviations = []

            # current cardinality
            cardinality = 8 * 2 ** i

            # algorithm h is incredibly inefficient and for cardinalities over 20 it takes too long to compute, this
            # conditional statement is to ensure the cardinality of algorithm h does not go too high
            if algorithm.__name__ == 'algorithm_h':
                cardinality = (i+1)*2

            # run each cardinality 1000 times, generate 1000 random arrays for testing
            for i in range(1000):

                # initialise array of random elements
                random_array = []

                # number of elements to be added to array
                for i in range(cardinality):
                    # elements are integers between 10*cardinality and 100*cardinality
                    random_array.append(random.randint(10*cardinality,
                                                       100*cardinality))

                # use current algorithm on current array
                s1, s2 = algorithm(random_array)

                # find deviation from ideal partition for current run through
                deviation_from_ideal = abs(sum(s1) - sum(s2)) // 2

                # store deviation from ideal in a list
                temp_list_deviations.append(deviation_from_ideal)

            # calculate mean deviation from ideal for current cardinality
            mean_deviation = sum(temp_list_deviations) // 1000

            # calculate standard deviation for current cardinality
            standard_deviation = statistics.stdev(temp_list_deviations)//1

            # add to correct lists if algorithm a is being iterated
            if algorithm.__name__ == 'algorithm_a':
                list_mean_deviations_a.append(mean_deviation)
                global list_standard_deviations_a
                list_standard_deviations_a.append(standard_deviation)

            # add to correct lists if algorithm b is being iterated
            elif algorithm.__name__ == 'algorithm_b':
                list_mean_deviations_b.append(mean_deviation)
                global list_standard_deviations_b
                list_standard_deviations_b.append(standard_deviation)

            # add to correct lists if algorithm c is being iterated
            elif algorithm.__name__ == 'algorithm_c':
                list_mean_deviations_c.append(mean_deviation)
                global list_standard_deviations_c
                list_standard_deviations_c.append(standard_deviation)

            # add to correct lists if algorithm d is being iterated
            elif algorithm.__name__ == 'algorithm_d':
                list_mean_deviations_d.append(mean_deviation)
                global list_standard_deviations_d
                list_standard_deviations_d.append(standard_deviation)

            # add to correct lists if algorithm e is being iterated
            elif algorithm.__name__ == 'algorithm_e':
                list_mean_deviations_e.append(mean_deviation)
                global list_standard_deviations_e
                list_standard_deviations_e.append(standard_deviation)

            # add to correct lists if algorithm f is being iterated
            elif algorithm.__name__ == 'algorithm_f':
                list_mean_deviations_f.append(mean_deviation)
                global list_standard_deviations_f
                list_standard_deviations_f.append(standard_deviation)

            # add to correct lists if algorithm g is being iterated
            elif algorithm.__name__ == 'algorithm_g':
                list_mean_deviations_g.append(mean_deviation)
                global list_standard_deviations_g
                list_standard_deviations_g.append(standard_deviation)

            # add to correct lists if algorithm h is being iterated
            elif algorithm.__name__ == 'algorithm_h':
                list_mean_deviations_h.append(mean_deviation)
                global list_standard_deviations_h
                list_standard_deviations_h.append(standard_deviation)

            # add to correct lists if algorithm i is being iterated
            elif algorithm.__name__ == 'algorithm_i':
                list_mean_deviations_i.append(mean_deviation)
                global list_standard_deviations_i
                list_standard_deviations_i.append(standard_deviation)


# takes a list of standard deviations as input to calculate the error bars for each cardinality
def calculate_error_bars(list_standard_deviations):
    # initialise errors list
    errors_list = []

    # there are 8 elements in input list
    for i in range(0, 8):

        # current cardinality
        cardinality = 8 * 2 ** i

        # calculate error by dividing the standard deviation by the square root of the number of samples
        error = list_standard_deviations[i] / math.sqrt(cardinality)

        # add to list of errors
        errors_list.append(error)

    return errors_list


# runs test harness
test_harness(list_algorithms)

# values on x-axis (the cardinalities)
x = (8, 16, 32, 64, 128, 256, 512, 1024)

# values on y-axis (average deviation from ideal partition)
y1 = list_mean_deviations_a
y2 = list_mean_deviations_b
y3 = list_mean_deviations_c
y4 = list_mean_deviations_d
y5 = list_mean_deviations_e
y6 = list_mean_deviations_f
y7 = list_mean_deviations_g
y8 = list_mean_deviations_h
y9 = list_mean_deviations_i

# error bar values for each algorithm
errors_a = calculate_error_bars(list_standard_deviations_a)
errors_b = calculate_error_bars(list_standard_deviations_b)
errors_c = calculate_error_bars(list_standard_deviations_c)
errors_d = calculate_error_bars(list_standard_deviations_d)
errors_e = calculate_error_bars(list_standard_deviations_e)
errors_f = calculate_error_bars(list_standard_deviations_f)
errors_g = calculate_error_bars(list_standard_deviations_g)
errors_h = calculate_error_bars(list_standard_deviations_h)
errors_i = calculate_error_bars(list_standard_deviations_i)

# plots each algorithm on the same graph
plt.errorbar(x, y1, yerr=errors_a, marker='x', mfc='red', capsize=4, label='Algorithm A', elinewidth=0.25, linewidth=0.25)
plt.errorbar(x, y2, yerr=errors_b, marker='x', mfc='orange', capsize=4, label='Algorithm B', elinewidth=0.25, linewidth=0.25)
plt.errorbar(x, y3, yerr=errors_c, marker='x', mfc='yellow', capsize=4, label='Algorithm C', elinewidth=0.25, linewidth=0.25)
plt.errorbar(x, y4, yerr=errors_d, marker='x', mfc='green', capsize=4, label='Algorithm D', elinewidth=0.25, linewidth=0.25)
plt.errorbar(x, y5, yerr=errors_e, marker='x', mfc='blue', capsize=4, label='Algorithm E', elinewidth=0.25, linewidth=0.25)
plt.errorbar(x, y6, yerr=errors_f, marker='x', mfc='indigo', capsize=4, label='Algorithm F', elinewidth=0.25, linewidth=0.25)
plt.errorbar(x, y7, yerr=errors_g, marker='x', mfc='violet', capsize=4, label='Algorithm G', elinewidth=0.25, linewidth=0.25)
plt.errorbar(x, y8, yerr=errors_h, marker='x', mfc='magenta', capsize=4, label='Algorithm H', elinewidth=0.25, linewidth=0.25)
plt.errorbar(x, y9, yerr=errors_i, marker='x', mfc='aquamarine', capsize=4, label='Algorithm I', elinewidth=0.25, linewidth=0.25)

# add legend
plt.legend(loc='upper left')

# label graph
plt.xlabel('Cardinality')
plt.ylabel('Mean deviation')
plt.title('Mean deviations at different cardinalities')
plt.xticks(x)

# show graph
plt.show()
