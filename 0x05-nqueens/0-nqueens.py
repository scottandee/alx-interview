#!/usr/bin/python3
"""Solve Nqueens"""

import sys

n = sys.argv[1]

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    int(n)
except ValueError:
    print("N must be a number")
    exit(1)

if int(n) < 4:
    print("N must be at least 4")
    exit(1)
n = int(n)
# col = []
# pos_diag = []
# neg_diag = []

# result = []
# board = []

# def backtrack(r):
#     if r == n:
#         result.append(board)
#         board.clear()
#         return
#     for c in range(n):
#         if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
#             continue
#         col.append(r)
#         pos_diag.append(r + c)
#         neg_diag.append(r - c)
#         board.append([r, c])

#         backtrack(r + 1)

#         col.remove(r)
#         pos_diag.remove(r + c)
#         neg_diag.remove(r - c)
#         board.remove([r, c])
# backtrack(0)

# for r in result:
#     print(r)
