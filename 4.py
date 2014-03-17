# PROBLEM: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# SOLUTION: a palindromic number with 2k+1 digits is sum over i from 0 to k, (a_i * 10^i + a_i * 10^(2k -i))
def is_palindromic(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] != n[len(n)- i - 1]:
            return False
    return True

def all_palindromic_products():
    palindromes = []
    for i in range(100,1000):
        for j in range(i,1000):
            if is_palindromic(i*j):
                palindromes.append((i,j, i*j))
    return palindromes

def largest_palindromic_product():
    return sorted(all_palindromic_products(), key= lambda p: p[-1]).pop()

if __name__ == "__main__":
    print largest_palindromic_product()

