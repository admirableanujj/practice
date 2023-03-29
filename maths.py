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


