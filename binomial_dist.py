#import math
#from math import *
from math import factorial
 
def binomial(n, k):
        if n >= k:
                b = factorial(n) / (factorial(k)*factorial(n-k))
                return b

def binomial_dist(n, p):
    return [binomial(n, k) * p**k * (1.0 - p)**(n-k) for k in range(0, n + 1)]
    
dist = binomial_dist(10, 0.8)
print(dist)
print(sum(dist))



    
