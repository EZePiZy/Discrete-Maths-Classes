def findbest(n):
    processed = set()
    unprocessed = set([frozenset([1])])
    while len(unprocessed):
        for x in list(unprocessed):
            xs = sorted(list(x), reverse=True)
            for a in xs:
                for b in xs:
                    y = x.union(frozenset([a+b]))
                    if n in y:
                        return y
                    if y in processed or y in unprocessed:
                        continue
                    unprocessed.add(y)
            processed.add(x)
            unprocessed.remove(x)


print(findbest(251))

import numpy # library to do numerical computations

def fib_matrix(n):
    if n<=2:
        return 1
    n = n-1 # we only need M^(n-1) to compute F(n)
    z = M = numpy.matrix([[1, 1], [1, 0]])
    y = I = numpy.matrix([[1, 0], [0, 1]])
    while n:
        if n & 1: # extract last bit of n
            y = y*M
        n = n >> 1 # shift n to the right
        M = M*M
    return y[0, 0]

#print(fib_matrix(27))
# print(list(map(F, range(1, 10))))