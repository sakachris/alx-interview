#!/usr/bin/env python3
''' 0-minoperations.py '''


def minOperations(n):
    '''
    returning minimum operations
    '''
    if n <= 1:
        return 0

    min_ops = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            min_ops += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        min_ops += n

    return min_ops
