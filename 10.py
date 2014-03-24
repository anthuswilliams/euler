import math, array

def eratosthenes(n):
  sieve = array.array('I',[True]*(n - 2))
  for k,v in enumerate(sieve):
    step = k + 2 # we want to start with 2, not 0
    if v:
      yield step
      j = step**2
      while j < n:
        sieve[j - 2] = False
        j += step

if __name__ == "__main__":
  print sum(eratosthenes(2*10**6))
