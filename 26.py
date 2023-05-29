# for x in range(0,40):    
#     divisor =  x
#     dividend = 1
#     remainder = dividend%divisor
#     while remainder !=0:
        
# =============================================================================
n = 1000
max_itteration = 20
unit_fraction = {}
# ============================================PART1(find quotie):
for x in range(1,n+1):
    count = 0         
    num_after_decimal = []
    divisor =  x
    dividend = 1
    # temp.append(int(dividend/divisor))
    # temp.append('.')
    reminder = dividend%divisor
    while reminder !=0:
        dividend=dividend*10
        y = int(dividend/divisor)
        num_after_decimal.append(int(dividend/divisor))
        reminder = dividend%divisor
        dividend = reminder 
        if count > max_itteration:
            break
        else:
            count +=1
    unit_fraction[x] = num_after_decimal
# print(unit_fraction)
# ============================================PART2(find recurring digits):
for key in unit_fraction.keys():
    quotient = unit_fraction[key]
    if len(quotient) > len(set(quotient)):
        print(f"{key}:{quotient}")
        no_of_rep_dgts = len(set(quotient))
        continue

    print(f'{key}:{quotient}--Not recurring')

# ================================================================
# """Ok it seems this question requires an algorithm to get soved, So, how to wirte that,
# I just want you to solve it using one accepatable approach once then we can look into peoples solution.
# So, my proposed solution would be: A three/two stage algorithm which, divides the problem into chunks,
# 1st part to be soved is a function that can find the quotient till the nth term.
# 2nd part to find recurring cycle in this quotient using the finite nth term
# 3rd find the number with the max number of recurring cycle. """