# PROBLEM: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc. 
#
import math

print int(reduce(lambda a,b: a*b, [[a,b,math.sqrt(a**2 + b**2)] for a in range(501) for b in range(a,501) if a + b + math.sqrt(a**2 + b**2) == 1000].pop()))
