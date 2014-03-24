# PROBLEM:  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
#
# SOLUTION: Wilson's theorem states p is prime iff (p - 1)! = (p-1) modulo p
#
# a^p - a = 0 mod p
import math

primes_so_far = [2,3]

# find all primes up to n
def eratosthenes(n):
  sieve = range(5,n)
  for p in primes_so_far:
    sieve = filter(lambda x: x % p != 0, sieve)
  while sieve:
    p = sieve.pop(0)
    primes_so_far.append(p)
    if p < math.sqrt(n): sieve = filter(lambda x: x % p != 0, sieve)
  return primes_so_far

if __name__ == "__main__":
  n = 60**2
  while len(primes_so_far) < 10001:
    n *= 2
    eratosthenes(n)
  print primes_so_far[10000]
