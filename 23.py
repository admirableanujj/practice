from maths import quick_math


# print(quick_math.factors(28123))
def checkAbundantNumber(x):
    factors =  quick_math.factors(x)
    if sum(factors) > x:
        return True
    return False

upper_limit = 28123
ls_of_abundant_num = []
ans = {}
for i in range(1,upper_limit+1):
    for j in range(1,i):
        x = i - j
        if checkAbundantNumber(j) and checkAbundantNumber(x):
            # ls_of_abundant_num.append(i)
            ans[i] = [x,j]
            break
    
        ans[i] = None
    print(f'i:{i}||{len(ans)}')

total = 0
for key in ans.keys():
    if ans[key]:
        continue
    else:
        print(key)
        total+=key
    
print(total)