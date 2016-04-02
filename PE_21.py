# Amicable numbers
import math
def d(x):
    l = 1
    end = int(math.sqrt(x))
    for i in range(2, end):
        if (x%i == 0):
            l += (i + x/i)
    return l

print sum([i for i in range(1,10000) if ((i == d(d(i))) and (i != d(i)))])
