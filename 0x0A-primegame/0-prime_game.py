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
        prime = [True for i in range(nums[r] + 1)]
        p = 2
        while (p * p <= nums[r] + 1):
            if (prime[p] == True):
                for i in range(p * p, nums[r] + 1, p):
                    prime[i] = False
            p += 1
        list = []
        for p in range(2, nums[r] + 1):
            if prime[p]:
                list.append(p)
        print(list)
        winner = ''
        if len(list) == 0:
            ben += 1
            continue
        for j in range(len(list)):
            if list[j] == 0: 
             continue
            num = list[j]
            list[j] = 0
            for j in range(j, len(list)):
                if list[j] % 2 == 0:
                    list[j] = 0
            if (j + 1) % 2 != 0:
                winner = 'Ben'
            else:
                winner = 'Maria'
        print(winner)
        if winner == "Maria":
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return 'Maria'
    elif maria == ben:
        return None
    else:
        return 'Ben'