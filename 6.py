# PROBLEM: The sum of the squares of the first ten natural numbers is,
# 
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)^2 = 55^22 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 485 = 2640
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
# SOLUTION: (x + y + z)^2 = x^2 + 2xy + 2yz + 2xz + y^2, hence the difference is 2(xy + xz + yz)
import itertools

def sum_squared_minus_sum_of_squares(nums):
    return 2 * sum([t[0] * t[1] for t in itertools.combinations(nums, 2)])

if __name__ == "__main__":
    print sum_squared_minus_sum_of_squares(range(101))
