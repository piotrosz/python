from math import *

def binomial_coef(n, k):
    result = factorial(n)/(factorial(k) * factorial(n - k))
    return result
