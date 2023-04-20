n = 0
fibonacci = [1,1]
next_num = None

# Recursion
# def fibonacci_se(n):
#     if n <=1 :
#         return n
#     return(fibonacci_se(n-1)+fibonacci_se(n-2))

# def fibonacci_se(n):

#     if n[0] < 0 or n[1]<0:
#         return None
#     if n[0] == 0 and n[1] == 1 :
#         return (1,1)
#     if n[0] == 1 and n[1] == 1 :
#         return (2,1)
#     return fibonacci_se((n[1]+n[0],n[1]))

# # =======Below is a very basic approach: Simple logic what actually the series means
def fibonacci_se(n):
    # global next_num
    i=0
    last_num = i + 1
    cur_num = last_num + i 
    while i < n:
        next_num =  cur_num +last_num
        last_num = cur_num
        cur_num = next_num
        i+=1
    # if next_num is not None:
    #     return next_num
    # return n
    return cur_num +last_num


# print(len(str(fibonacci_se(11))))

i=0
r=3
# x = (1,0)
while n < 1000:
    x = fibonacci_se(i)
    n  = len(str(x))
    print(f'f({r})||i:{i}:{x}')
    i +=1
    r +=1
    
print(f'r:{r}')        


            
###############################################################################################################
# while len(str(fibonacci[0])) < 3:
#     fibonacci = [1,1]
#     for i in range(0,n):    
#         if i <2:
#             fibonacci.append(1)
#             continue
#         fibonacci.append(fibonacci[i-1]+fibonacci[i-2])    
#     n +=1