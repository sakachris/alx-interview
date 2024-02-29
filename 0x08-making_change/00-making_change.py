#!/usr/bin/python3
"""
Module for making change using dynamic programming
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the given total amount.
    """
    if total < 1:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
