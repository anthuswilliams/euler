# PROBLEM: The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# SOLUTION: The Pollard Rho algorithm wil work quickly for numbers this size. Don't try it on extremely large (100+ digits) numbers if you value your time
#
# Start with a random 1 < x_0 < n, and for i = 1,2,3,...  take x_i = x_(i-1)^2 - 1 (mod n) and d_i = GCD(n, x_(2i) - x_i)
import random

memoized_primes = []

def largest_prime(n):
    if is_prime(n):
        return n
    factors = divisors(n)
    factors.sort()
    while not is_prime(factors[-1]):
        factors.sort()
        factors.append(largest_prime(factors.pop()))
    return factors.pop()

def divisors(n):
    if is_prime(n):
        return [n]
    x_0 = random.randint(0, n)
    d_i = 1
    def x_i(i, x = n):
        if i == 0:
            return x
        return (x_i(i - 1, x_0)**2 - 1) % n
    i = 0
    while d_i == 1:
        i += 1
        d_i = gcd(n, ( x_i(2*i, x_0) - x_i(i, x_0) ))
        if d_i == n:
            x_0 = random.randint(0,n)
            d_i = 1
            i = 0
    return [d_i, n/d_i]

def is_probably_prime(n, r):
    # first, we seek a k and d so that we can write n - 1 = d * (2^k)
    k = 0
    while True:
        if (n - 1) % (2**( k+1 )) != 0: # seeking the largest k such that 2^k divides n - 1
            break
        k += 1
    d = (n -1)/(2**k)
    if d > 1:
        factors = [d]
        multipliers = []
        while factors:
            for f in factors:
                factors.remove(f)
                if f <= 10000000 or is_prime(f):
                    multipliers.append(f)
                else:
                    factors.extend(divisors(f))
        for f in multipliers:
            r = (r ** f) % n
    if r == 1 or r == n - 1:
        return True
    for s in range(k):
        r = (r ** 2) % n
        if r == 1:
            return False
        if r == n - 1:
            return True
    return False

def is_prime(n):
    if n in memoized_primes:
        return True
    if n > 341550071728321:
        raise "Yeah, I don't know if this is prime or not!"
    for a in [2,3,5,7,11,13,17]: 
        # if n passes is_probably_prime for each of these witnesses and is less than 341,550,071,728,321, then it is deterministically prime
        # this is due to a result by Pomerance, Wagstaff, Selfridge, and Jaeschke
        if not is_probably_prime(n, a):
            return False
    memoized_primes.append(n)
    return True
        
def gcd(a, b):
    m = 1
    if a <= 0 and b <= 0:
        m = -1 # if both are < 0, then -1 is a common divisor
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return m * max(a, b)
    if a % 2 == 0 and b % 2 == 0:
        return 2 * m * gcd(a/2, b/2) # if both are even, 2 is a common divisor
    elif b % 2 == 0:    
        return m * gcd(a, b/2) # a is odd, so 2 is not a common divisor
    elif a % 2 == 0:
        return m * gcd(a/2, b)
    else:
        return m * gcd(abs(b-a)/2, min(a,b))

if __name__ == "__main__":
    print largest_prime(600851475143)
