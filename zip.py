# avg

p = [0.5, 0.4, 0.3]
n = [12, 42, 56]

print( sum([ x[0]*x[1] for x in zip(p, n)]) )


print( sum(a * b for a, b in zip(p, n)) )
    
