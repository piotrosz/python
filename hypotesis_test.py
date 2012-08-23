from __future__ import division
from math import sqrt

def mean(data):
    return sum(data)/len(data)

def var(data):
    return sum((x - mean(data))**2 for x in data)  / len(data)

def dev(data):
    return sqrt(var(data))

def factor(data):
    return 1.96

def CI(data):
    return factor(data) * dev(data) / sqrt(len(data))

def test(data, h):
    #if(h < mean(data) + CI(data) and h > mean(data) - CI(data)) :
    #    return 1
    #else :
    #    return 0
    return abs(h - mean(data)) <= CI(data)
    
data = [21] * 4 + [24] * 6 + [26] * 7 + [29] * 11 + [40] * 2

print(mean(data))
print(var(data))
print(CI(data))

h = 26
print(test(data, h))
