from maths import quick_math
n = 8
truncatable_primes = []

def check_right_to_left(num):
    for i in range(1,len(str(num))):
        new_num = num//10**i
        if not quick_math.isprime(new_num):
            return False
    return True
        
def check_left_to_right(num):        
    for i in range(1,len(str(num))):
        new_num = num%10**i
        if not quick_math.isprime(new_num):
            return False
    return True


""" it can be rewritten for a faster approch 
    compare methods if "and" or "or" can be used to compare both sides together with floor divide and remainer operations.
"""
base_prime = [2,3,5,7]
while len(truncatable_primes) <= 10 :
    if n%10 in base_prime:
        if check_left_to_right(n): 
            print(f'n:{n}||lenght:{len(truncatable_primes)}||list: {truncatable_primes}||{sum(truncatable_primes)}')
            if check_right_to_left(n):
                if quick_math.isprime(n):
                    truncatable_primes.append(n)
                    print(' ')
    n+=1       
    
print(f'required list: {truncatable_primes}||len:{len(truncatable_primes)}||ans{sum(truncatable_primes)}')
