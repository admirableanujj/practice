# In this question you can develop a permutation of all the numbers and then keep moving the multiplication and equal to sign from right to left 
# and based on it check if the product is equivalent to RHS. In case it does that number is the number of interest.
# can use recursion to develop a chain of numbers with it.
import maths

digits_available = []
for i in range(1,10):
    digits_available.append(i)
digits_available = tuple(digits_available)
# print(digits_available)

possible_permutation = maths.quick_math.permutation(len(digits_available),len(digits_available))
available_permutation = []

#n is a set of elements available.
###############################################
def find_permutations(data_list):
    if not data_list:
        return []
    if len(data_list)==1:
        return [data_list]
    sol_list = [] #empty list to store data
    for i in range(len(data_list)):
        m = data_list[i]
        rem_list  = data_list[:i] +data_list[i+1:]
        for p in find_permutations(rem_list):
            sol_list.append([m]+p)
    return sol_list
    
    
def check_pandigital_product(num, ran):
    sol_list = []
    for i in range(1,ran-1):
        for j in range(i+1,ran):
            multiplicand = ''.join(str(x) for x in num[0:i])
            multiplier = ''.join(str(x) for x in num[i:j])
            product = ''.join(str(x) for x in num[j:])
            # print(f'{multiplicand}X{multiplier}={product}')
            if int(multiplicand)*int(multiplier) == int(product):
                sol_list.append([multiplier,multiplicand,int(product)])
    return sol_list
        
    
n = [1,2,3,4,5,6,7,8,9]
# print(find_permutations(n))
y = set()
for i in find_permutations(n):
    x = check_pandigital_product(i,len(i))
    if x :
        print(f'x:{x}')
        y.add(x[0][2])

print(f'Ans:{sum(y)}')        


    
    
    
    
    
###############################################
# def find_possible_permutations(fixed, n, permutations):
#     try:
#         num = len(n)
#     except TypeError as e:
#         return e
#     if num == 2:
#         e1= fixed + [n[0],n[1]]
#         e2= fixed + [n[1],n[0]]
        
#         permutations.append(''.join(str(x) for x in e1))
#         permutations.append(''.join(str(x) for x in e2))
#         # permutations.append(e1)
#         # permutations.append(e2)
#         return permutations
#     elif num >2:
#         additional_digits = num - 2
#         for i in range(0,additional_digits):
#             fixed.append(n[i])
#             x = n[:]
#             x.remove(n[i])
#             # print(f'fixed:{fixed}||n:{n}||x:{x}||i{i}')
#             find_possible_permutations(fixed,x,permutations)
#     return permutations
 


# n = [1,2,3,4]
# for i in range(0,len(n)):
#     a = [n[i-len(n)],n[1+i-len(n)],n[2+i-len(n)],n[3+i-len(n)]]
#     # print(a)
#     print(find_possible_permutations([],a,[]))

# while len(available_permutation) < possible_permutation:
#     pass





