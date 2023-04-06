# improve to a faster function later


class quick_math:
    def __init__(self):
        factors =  None

    @staticmethod
    def factors(x):
        factors = []
        for i in range(1,x):
            if x%i == 0:
                factors.append(i)
        return factors
    
    @staticmethod
    def factorial(x):
        if x<1:
            return 1 
        return x*quick_math.factorial(x-1)
    
    @staticmethod
    def permutation(n,r):
        return quick_math.factorial(n)/quick_math.factorial(n-r)
    @staticmethod
    def combination(n,r):
        divisor = quick_math.factorial(r)*quick_math.factorial(n-r) 
        return quick_math.factorial(n)/divisor
        