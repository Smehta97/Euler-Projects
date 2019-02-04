import math
def primeFactors(n):
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0: # is factor
            print i
            n = n / i

primeFactors(600851475143)
