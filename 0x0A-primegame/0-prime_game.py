#!/usr/bin/python3
""" Prime Game """


def is_prime(n):
    """ checking if prime number """

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def calculate_primes_up_to(n):
    """ calculates prime numbers upto n """

    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)

    return primes


def isWinner(x, nums):
    """ determines the winner of each game """

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = calculate_primes_up_to(n)
        if len(primes) % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] == wins["Ben"]:
        return None

    return max(wins, key=wins.get)
