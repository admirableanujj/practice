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
P1010 = int(permutation(10,10))
print(f'P1010 = {P1010}')
print(f'rank = {rank}||rank/P1010 = {rank/P1010}')
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P1010) * P1010
print('=====================================================')

P99  = int(permutation(9,9))
print(f'P99 = {P99}')
print(f'rank = {rank}||rank/P99 = {rank/P99}')
ans.append(given.pop(int(rank/P99)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans} || ')
rank = rank - int(rank/P99) * P99
print('=====================================================')

P88  = int(permutation(8,8))
print(f'P88 = {P88}')
print(f'rank = {rank}||rank/P88 = {rank/P88}')
ans.append(given.pop(int(rank/P88)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P88) * P88
print('=====================================================')

P77  = int(permutation(7,7))
print(f'P77 = {P77}')
print(f'rank = {rank}||rank/P77 = {rank/P77}')
ans.append(given.pop(int(rank/P77)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P77) * P77
print('=====================================================')

P66  = int(permutation(6,6))
print(f'P66 = {P66}')
print(f'rank = {rank}||rank/P66 = {rank/P66}')
ans.append(given.pop(int(rank/P66)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P66) * P66
print('=====================================================')

P55  = int(permutation(5,5))
print(f'P55 = {P55}')
print(f'rank = {rank}||rank/P55 = {rank/P55}')
ans.append(given.pop(int(rank/P55)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P55) * P55
print('=====================================================')

P44  = int(permutation(4,4))
print(f'P44 = {P44}')
print(f'rank = {rank}||rank/P44 = {rank/P44}')
ans.append(given.pop(int(rank/P44)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P44) * P44
print('=====================================================')

P33  = int(permutation(3,3))
print(f'P33 = {P33}')
print(f'rank = {rank}||rank/P33 = {rank/P33}')
ans.append(given.pop(int(rank/P33)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P33) * P33
print('=====================================================')

P22  = int(permutation(2,2))
print(f'P22 = {P22}')
print(f'rank = {rank}||rank/P22 = {rank/P22}')
ans.append(given.pop(int(rank/P22)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P22) * P22
print('=====================================================')

P11  = int(permutation(1,1))
print(f'P11 = {P11}')
print(f'rank = {rank}||rank/P11 = {rank/P11}')
ans.append(given.pop(int(rank/P11)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P11) * P11
print('=====================================================')

P00  = int(permutation(0,0))
print(f'P00 = {P00}')
print(f'rank = {rank}||rank/P00 = {int(rank/P00)}')
ans.append(given.pop(int(rank/P00)))
print(f'given:{given}||len(given):{len(given)}||ans:{ans}')
rank = rank - int(rank/P00) * P00
print('=====================================================')


print(2783915460)
