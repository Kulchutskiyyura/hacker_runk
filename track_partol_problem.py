#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def find_answer(petrol, distance, n):
    start, sum_ = 0, 0
    for i in range(n):
        sum_ += petrol[i] - distance[i]
        if sum_ < 0:
            start = i + 1
            sum_ = 0

    return start


def truckTour(input_):
    petrol, distance = [], []

    n = len(input_)

    for i in range(n):
        p, d = input_[i]
        petrol.append(p), distance.append(d)

    return find_answer(petrol, distance, n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
