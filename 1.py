#PROBLEM: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

# SOLUTION: The sequences 3n and 5n are arithmetic progressions
#                    so their sum up to the kth term can be computed k(d +dk)/2, where d is the divisor
# This  solution is O(1)! YAY
def number_crunch(n):
    multiplier = 1
    if n < 0:
        multiplier = -1
    n = abs(n)
    def series_sum(n,d):
        # subtract 1 from our n because the problem says we are to only consider numbers BELOW 1000 which are divisible by 3 or 5
        k = (n - 1)//d # k is the number of terms
        return k*d*(1 + k)/2 # k(d + dk)/2 is the formula for the partial sum of arithmetic series
    return (series_sum(n,3) + series_sum(n,5) - series_sum(n,15)) * multiplier


if __name__ == '__main__':
    print(number_crunch(1000))
    print(number_crunch(10**350))
