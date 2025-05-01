#Digital Cancelling Fractions
from maths import quick_math as m
curious_fractions = set()
for i in range(10,100):
    for j in range(10,100):
        if i == j:
            continue
        if i % 10 == 0 and j % 10 == 0:
            continue
        if i % 10 == j // 10:
            numerator_10 = i // 10
            denominator_1 = j % 10
            if denominator_1 and numerator_10 /denominator_1 == i/j:
                curious_fractions.add(frozenset([i,j]))
        if i // 10 == j % 10:
            numerator_1 = i // 10
            denominator_10 = j % 10 
            if numerator_1 and numerator_1 /denominator_10 == i/j:
                curious_fractions.add(frozenset([i,j]))



the_four = []
for curious_fraction in list(curious_fractions):
    curious_fraction = list(curious_fraction)
    curious_fraction.sort()
    i = curious_fraction[0]
    j = curious_fraction[1]
    if i/j < 1:
        the_four.append(curious_fraction)
n = 1
d = 1
for i in the_four:
    n *= i[0]
    d *= i[1]
    print(i)
# print(f'Curious Fractions: {the_four}')
# print(f'numerator: {n}|| denominator: {d}')
n_factors = m.factors(n)
d_factors = m.factors(d)
jj = []
for i in range(1,n):
    if d%i == 0:
        jj.append(i)

print(jj)
print(f"ans:{d//jj[-1]}")

# for i in n_factors:
#     if i in d_factors:
#         n_factors.remove(i)
#         d_factors.remove(i)
# print(f'Unique factors of numerator: {n_factors}|| Unique factors of denominator: {d_factors}')
# print(f'Final numerator: {n}|| Final denominator: {d}')
print(len(the_four))




        