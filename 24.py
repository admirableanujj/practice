from maths import quick_math

def permutation(n,r):
    return quick_math.factorial(n)/quick_math.factorial(n-r)
# - millionith lexicographic permutation
given =  list(range(0,10))

# ===========================================
# ---------- if 10P10 > rank it has more than required options to fill.
# 0--------- Assuming 0 is the 1st number then total combinations possible 9P9(362880) Since it is less than required rank.
# it need to pass all starting with zero. 
# 1--------- is again 9P9 total combination possible 362880 which is still less than rank. Then let fix the next number and check.
# 2-------- is again 9P9 but now the combination is  more than 362880 so we will choose 2 
# 2 0-------- 8P8 >rank/10 8P* which is 40320. so trying to do with next available number. 
# 2 3 0-------
# 2 3 1-------
# 2 3 4-------
# 2 3 4 0------
# number = [2]
# ===========================================
rank = 1000000 -1
given = list(range(10))
ans = []
n = len(given)
r = n
while given and rank != 0:
    
    possible_permutation = int(permutation(n,r))
    print(f'P{n}{r} = {possible_permutation}')
    print(f'rank = {rank}||rank/P1010 = {rank/possible_permutation}')
    print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
    temp_rank = rank - int(rank/possible_permutation) * possible_permutation
    if temp_rank != rank:
            ans.append(given.pop(int(rank/possible_permutation)))
            rank = temp_rank
            n = len(given) 
            r = n
            continue 
    n = len(given) - 1
    r = n
    print('=====================================================')
ans.extend(given)
print(f'ans:{ans}')


print(2783915460)
