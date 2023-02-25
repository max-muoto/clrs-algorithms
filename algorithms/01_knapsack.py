from collections import defaultdict
from pprint import *


# O(w * n) time complexity
def knapsack(p, w, n, W):
    solutions = defaultdict(lambda: defaultdict(int))
    # O(n) where n = items
    for i in range(0, n):
        # O(w) where w = max weight
        for j in range(0, W + 1):
            if solutions[i - 1][j] >= solutions[i - 1][j - w[i]] + p[i]:
                if w[i - 1 + 1] <= j:
                    solutions[i][j] = solutions[i - 1][j]
            if solutions[i - 1][j - w[i]] + p[i] > solutions[i - 1][j]:
                if w[i - 1 + 1] + w[i + 1] <= j:
                    solutions[i][j] = solutions[i - 1][j - w[i]] + p[i]

    return solutions


def main():
    # Worth for each item in dollars
    p = [1, 2, 5, 6]
    # Weights for each item in pounds
    w = [2, 3, 4, 5]

    n = len(p)
    W = 8

    pprint(knapsack(p, w, n, W))


if __name__ == "__main__":
    main()
