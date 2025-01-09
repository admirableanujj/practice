from maths import quick_math as math
n = 0 
a = -999
b = -1000

ans_dict = {}
finol = {}
while a<1000:
    b = 0
    while b<=1000:
        x=n
        ans_list = []
        while math.isprime(x*x+a*x+b):
            ans_list.append(x*x+a*x+b)
            if a > 0:
                ans_dict[f'x*x+{a}x+{b}'] = ans_list
                finol[f'x*x+{a}x+{b}'] = len(ans_list)
            else:
                ans_dict[f'x*x{a}x+{b}'] = ans_list
                finol[f'x*x{a}x+{b}'] = len(ans_list)                
            x+=1
        
        b+=1
    a+=1

# print(ans_dict)
print(list(finol.keys())[list(finol.values()).index(max(finol.values()))])
print(ans_dict[list(finol.keys())[list(finol.values()).index(max(finol.values()))]])
    