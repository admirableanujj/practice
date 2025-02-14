coin_dict = { 
              1:0,
              2:0,
              5:0,
              10:0,
              20:0,
              50:0,
              100:0,
              200:0,
}
# ===============================================================================
# coin_types = coin_dict.keys()
# def coins_required(start_i, coin_types, target, result, temp):
#     print(f'{result}||{temp}')
#     if target == sum(temp):
#         # temp.append(coin_types[start_i-1])
#         result.append(tuple(temp))
#         return
#     if target > sum(temp) and start_i < len(coin_types):
#         # result.append(coin_types[start_i])
#         temp.append(coin_types[start_i])
#         return coins_required(start_i, coin_types, target, result, temp)
#         # return result
#     if start_i >=len(coin_types) or start_i >= len(temp):
#         return result
#     temp.pop(start_i)
#     start_i+=1

#     return coins_required(start_i, coin_types, target, result, temp)
# ===============================================================================
# def coins_required(start_i, coin_types, target, result, temp):
#     print(f'{result}||{temp}')
#     if sum(temp) == target:
#         result.append(tuple(temp))
#         return 
#     if sum(temp) > target:
#             temp.pop(0)
#             coins_required(start_i+1, coin_types, target, result, temp)
#     temp.append(coin_types[start_i])
#     coins_required(start_i, coin_types, target, result, temp)
#     temp.pop()
#     coins_required(start_i+1, coin_types, target, result, temp)
#     return
# ===============================================================================            
def coins_required(start_i, coin_types, target, result, temp):
    temp.append(coin_types[start_i])
    # print(f'{result}||{temp}')
    if sum(temp) == target:
        result.append(temp[:])
        return result
    if sum(temp) > target:
        return result
    # coins_required(start_i, coin_types, target, result, temp)
    # temp.pop()
    for i in range(start_i,len(coin_types)):
        coins_required(i, coin_types, target, result, temp)
        temp.pop()
    return result




target = 200
coin_types = list(coin_dict.keys())
# coin_types = [2,3,6,7]
ans = []
for i in range(0,len(coin_types)):
    ans.append(coins_required(i,coin_types,target,[],[]))
# print(coins_required(0,coin_types,target,[],[]))
count = 0
for an in ans:
    print(len(an))
    count = count+len(an)

print(count)

