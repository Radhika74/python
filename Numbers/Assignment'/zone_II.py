
import math
import os
import random
import re
import sys

def min_moves_to_zero(n):
    if n == 0:
        return 0

    queue = [(n, 0)]
    visited = {n}
    front = 0

    while front < len(queue):
        num, moves = queue[front]
        front += 1

        if num == 0:
            return moves

        if num - 1 not in visited:
            queue.append((num - 1, moves + 1))
            visited.add(num - 1)

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                max_factor = max(i, num // i)
                if max_factor not in visited:
                    queue.append((max_factor, moves + 1))
                    visited.add(max_factor)

def solve():
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(min_moves_to_zero(n))

solve()