from maths import quick_math

def checkAbundantNumber(x):
    factors =  quick_math.factors(x)
    if sum(factors) > x:
        return True
    return False
total = 0
upper_limit = 28123
ls_of_abundant_num = []
ans = {}
for i in range(0,upper_limit+1):
    for j in range(0,i):
        x = i - j
        if checkAbundantNumber(j) and checkAbundantNumber(x):
            # ls_of_abundant_num.append(i)
            ans[i] = [x,j]
            break
        ans[i] = None
    print(f'i:{i}||{len(ans)}')
#calculating None in the dict
for key in ans.keys():
    if ans[key]:
        continue
    else:
        print(key)
        total+=key
print(total)