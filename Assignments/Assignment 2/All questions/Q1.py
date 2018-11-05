'''Write a short Python function that takes a positive 
   integer n and returns the sum of the squares of
   all the odd positive integers smaller than n.'''


def OddPowerSum(n):
    t = 0
    for a in range(n):
        if a%2 != 0:
            t = t + a*a
    return t


print(OddPowerSum(12))
print(OddPowerSum(5))
