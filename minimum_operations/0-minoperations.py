#!/usr/bin/python3
"""
a technique that uses the operations Copy All and Paste as its only operations to determine how few operations are necessary to produce exactly n copies of a character in a text file.
"""


def minOperations(n):
    """Create sum"""
    
    if type(n) is not int or n <= 1:
        return 0
    operations_sum = []
    divisor = 2
    while (n % divisor) is 0 and (n // divisor) is not 1:
        operations_sum.append(divisor)
        n = n // divisor
    divisor = 3
    while n > divisor:
        while (n % divisor) is 0 and (n // divisor) is not 1:
            operations_sum.append(divisor)
            n = n // divisor
        divisor += 2
    operations_sum.append(n)
    return sum(operations_sum)
