def repeating_number(x):
    # x -- divisor
    dividend = 1
    quotient = []
    num_rem = set()
    while True:
        num = dividend//x
        remainder = dividend%x
        quotient.append(num)
        if remainder in num_rem:
            break
        num_rem.add(remainder)
        dividend = remainder*10
    return quotient[1:]

max_recurring = 0
number = 0
for x in range(2,1000):
    # print(f'{x}:{repeating_number(x)}')
    quotient = repeating_number(x)
    if max_recurring < len(quotient):
        max_recurring = len(quotient)
        number = x
        
print(f'max_recurring: {max_recurring}||number:{number}')
    



###################################################################################################################
# works only upto cetain number need some more work. 
###################################################################################################################
# for x in range(0,40):    
#     divisor =  x
#     dividend = 1
#     remainder = dividend%divisor
#     while remainder !=0:
        
# # =============================================================================
# n = 17
# max_itteration = 1000
# unit_fraction = {}
# ============================================PART1(find quotie):

# def check_repeating(x_lst, itterations):
#     count = 0
#     temp = []
#     while len(x_lst) != len(set(x_lst)) and count <= itterations:
#         no_of_rep_dgts = len(set(x_lst))
#         for i in range(0, len(x_lst)-no_of_rep_dgts):
#             if x_lst[i:i+no_of_rep_dgts] == x_lst[i+no_of_rep_dgts:i+2*no_of_rep_dgts]:
#                 x_lst = x_lst[i:i+no_of_rep_dgts]
#                 count+=1
#                 break
#             temp.append(x_lst[i])
#             count+=1
#     temp.append(x_lst)
#     return temp
    

# for x in range(1,n+1):
#     count = 0         
#     num_after_decimal = []
#     divisor =  x
#     dividend = 1
#     # temp.append(int(dividend/divisor))
#     # temp.append('.')
#     reminder = dividend%divisor
#     while reminder !=0:
#         dividend=dividend*10
#         y = dividend//divisor
#         num_after_decimal.append(dividend//divisor)
#         reminder = dividend%divisor
#         dividend = reminder 
#         if count > max_itteration:
#             break
#         else:
#             count +=1
#     unit_fraction[x] = num_after_decimal
# # print(unit_fraction)
# # ============================================PART2(find recurring digits):
# for key in unit_fraction.keys():
#     quotient = unit_fraction[key]
#     if len(quotient) > len(set(quotient)):
#         quotient = check_repeating(quotient,max_itteration)
#         print(f"{key}:{quotient}")
#         unit_fraction[key] = quotient
#         continue
#     print(f'{key}:{quotient}--Not recurring')

# # ============================================PART3(max number of recurring cycle):
# key_with_max_recurring = 1
# len_key_with_max_recurring = 0
# for key in unit_fraction.keys():
#     if unit_fraction[key]:    
#         if isinstance(unit_fraction[key][-1],list):
#             if len(unit_fraction[key][-1]) >= len_key_with_max_recurring:
#                 key_with_max_recurring = key
#                 len_key_with_max_recurring = len(unit_fraction[key][-1])

# print(f'key_with_max_recurring:{key_with_max_recurring}|||len_key_with_max_recurring:{len_key_with_max_recurring}')
# ================================================================
# """Ok it seems this question requires an algorithm to get soved, So, how to wirte that,
# I just want you to solve it using one accepatable approach once then we can look into peoples solution.
# So, my proposed solution would be: A three/two stage algorithm which, divides the problem into chunks,
# 1st part to be soved is a function that can find the quotient till the nth term.
# 2nd part to find recurring cycle in this quotient using the finite nth term
# 3rd find the number with the max number of recurring cycle. """