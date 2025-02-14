import time
power = 5
number = 1
max_list_count = 6
ans_lst = []

start_time = time.time()
timeouttime = start_time + 60*3 #time in seconds

def totalOfDigits(number_instring):
    sum = 0
    for i in range(0, len(number_instring)):
        sum = sum + int(number_instring[i])**power
    
    return sum


# while len(ans_lst) < max_list_count:
#     number +=1
#     if totalOfDigits(str(number)) == number:
#         ans_lst.append(number)
#     if time.time() > timeouttime:
#         break
max_timeouttime = timeouttime
time_cookie = 10
while time.time() < max_timeouttime:
    while len(ans_lst) < max_list_count:
            number +=1
            if totalOfDigits(str(number)) == number:
                ans_lst.append(number)
                print(f'number:{ans_lst}||total:{sum(ans_lst)}')
                max_list_count+=1
                max_timeouttime=time.time()+60*time_cookie
            if time.time() > max_timeouttime:
                break



print(ans_lst)
print(f'answer:{sum(ans_lst)}')

