from maths import quick_math as m
from datetime import datetime as time
start_t = time.now()
print(f'start time:{start_t}')
upper_limit = 1000000
number = 2


def check_prime(x):
    if x <=1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
    
        
#this method needs to improve for duplicates
def possible_permutations(digit_arr):
    if not digit_arr:
        return []
    if len(digit_arr)<2:
        return [digit_arr]
    permutation = []
    for i in range(0, len(digit_arr)):
        fixed_digit = digit_arr[i]
        rem_arry = digit_arr[:i]+digit_arr[i+1:]
        for p in possible_permutations(rem_arry):
            permutation.append([fixed_digit]+p)
    return permutation

def circular_permutations(digit_arr):
    if not digit_arr:
        return []
    required_permutation = [digit_arr]
    while len(required_permutation) < len(digit_arr):
        curr_arry = required_permutation[-1]
        first_digit = curr_arry[0]
        rem_digits = curr_arry[1:]
        required_permutation.append(rem_digits+[first_digit])
        if required_permutation[-1] == digit_arr:
            break
    return required_permutation
        
        

circular_prime = []
prime_num = set()
while number<=upper_limit:
    # if not check_prime(number):
    #     number+=1
    digits = [x for x in str(number)]
    permutations = circular_permutations(digits)
    # #removing duplicates
    # temp_p = set()
    # for per in permutations:
    #     temp_p.add(tuple(per))
    all_prime_flag = False
    for p in permutations:
        num = int(''.join([str(x) for x in p]))
        if num in list(prime_num):
            all_prime_flag = True        
        else:            
            if check_prime(num):
                all_prime_flag = True
                prime_num.add(num)
            else:
                all_prime_flag = False
                break
    if all_prime_flag:
        circular_prime.append(permutations)
  
    number+=1
end_t = time.now()
cir_prime_num = set()
for c in circular_prime:
    print(c)
    temp = set()
    for num in c:
        x = int(''.join([str(x) for x in num]))
        temp.add(x)
    cir_prime_num.add(frozenset(temp))    
x= list(cir_prime_num)
x.sort()
print(f'{[list(y) for y in x]}||Len of x:{len(x)}')
print(f'total circular primes:{len(circular_prime)}')
print(f'end time:{end_t}||RunTime:{end_t-start_t}||upper_limit:{upper_limit}')

# [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 199, 311, 337, 373, 733, 919, 991]
# [2,3,5,7,11,13,17,31,37,71,73,79,97,113,199,337]