# first find factorials of number

n = 10000
factorials = []

def factorial(n):
    factorials = []
    for i in range(1,n):
        if n%i == 0:
            factorials.append(i)
    return factorials
amicable_num = {}
count = 0
# print(sum(factorial(284)))
for j in range(1,n):
    factors_a = factorial(j)
    factors_b  = factorial(sum(factors_a))
    if sum(factors_b) == j:
        amicable_num[j] = sum(factors_a)

# print(amicable_num)
for key in list(amicable_num.keys()):
    if key == amicable_num[key]:
        amicable_num.pop(key)
print(amicable_num)        
print(sum(amicable_num.keys()))        
