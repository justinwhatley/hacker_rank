
# Working, but too slow

"""
https://www.hackerrank.com/challenges/summing-pieces/problem

"""


import sys


def partition(number):
    # determines all possible partitions of n
    return {(x,) + y for x in range(1, number) for y in partition(number-x)} | {(number,)}


def summing_pieces(a, n, mod):
    indexes = (partition(n))
    total = 0
    for index in indexes:
        # print('index:' + str(index))
        outer_count = 0
        for size in index:
            # print('size: ' + str(size))
            inner_count = 0
            b_list = []
            while inner_count < size:
                # creates b_list from partition sizes
                b_list.append(a_list[outer_count]%mod)
                inner_count = inner_count + 1
                outer_count = outer_count + 1
            # performs the sum of elements in the list multiplied by the list size
            total = (total + sum(b_list)%mod*len(b_list))%mod
    return total


if __name__ == '__main__':
    data = sys.stdin.readlines()
    n = int(data[0])
    a_list = [int(x) for x in data[1].split(' ')]
    mod=(10**9)+7
    print(summing_pieces(a_list, n, mod))




