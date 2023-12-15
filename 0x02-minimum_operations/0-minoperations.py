#!/usr/bin/python3
"""This script conntains a function that  calculates
the fewest number of operations needed to result in
exactly `n` H characters in a file
"""


def minOperations(n: int) -> int:
    """function that  calculates the fewest
    number of operations needed to result in
    exactly `n` H characters in a file
    """
    total: int = 1
    ops: int = 0
    current: int = 0

    if n <= 0:
        return ops

    while True:
        if total + total <= n:
            current = total
            total += current
            ops += 2
        else:
            total += current
            ops += 1
        if n <= total:
            return ops
