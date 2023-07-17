from maths import quick_math

# "n^2 + an + b" Find ab such that 
max_prime = 1
for n in range(0,40):
    a = 1
    b = 1
    while a < 1000 and b <=1000:
        consecutive_prime = []
        for i in range(0,n):
            x = i**2 + a*i + b
            if quick_math.isprime(x):
                consecutive_prime.append(x)
        if max_prime < len(consecutive_prime):
            max_prime = len(consecutive_prime)
            print(f'(n^2+{a}n+{b})|:|{len(consecutive_prime)}|{consecutive_prime}')
        if b == 1000:
            a +=1
            b = 0
        b +=1
        # print(f'a:{a},b:{b}')
        # quick_math.progress_bar(a)
    