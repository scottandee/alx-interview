#!/usr/bin/python3
"""This script contains the solution
to the prime game problem
"""


def isWinner(x, nums):
    """Maria and Ben are playing a game. Given a
    set of consecutive integers starting from 1
    up to and including n, they take turns choosing a
    prime number from the set and removing that number
    and its multiples from the set. The player that
    cannot make a move loses the game.
    """
    ben = 0
    maria = 0

    for r in range(x):
        # Generate list of prime numbers between
        # 0 and n
        prime = [True for i in range(nums[r] + 1)]
        p = 2
        while (p * p <= nums[r] + 1):
            if prime[p] is True:
                for i in range(p * p, nums[r] + 1, p):
                    prime[i] = False
            p += 1
        list_of_primes = []
        for p in range(2, nums[r] + 1):
            if prime[p]:
                list_of_primes.append(p)

        # Ben wins the round if there are no primes
        # for Maria to choose
        if len(list_of_primes) == 0:
            ben += 1
            continue

        # Odd number of primes means Maria will win the round
        # while Even number of primes means Ben will win the round
        if len(list_of_primes) % 2 != 0:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return 'Maria'
    elif maria == ben:
        return None
    else:
        return 'Ben'
