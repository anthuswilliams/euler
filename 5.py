# PROBLEM: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# SOLUTION: mutliply greatest possible powers of prime factors together
import math

primes = [2,3,5,7,11,13,17,19]
factors = primes[:]

for n in [i for i in range(2,21) if not i in primes]:
    for i, p in enumerate([p for p in primes if p <= math.sqrt(n)]): # only consider primes that can potentially be a factor of n
        exp = p
        if n % exp != 0: continue
        while n % (exp*p) == 0: exp *= p # find the largest power of p that divides n
        if factors[i] < exp: factors[i] = exp

print reduce(lambda a,b: a*b, factors)
