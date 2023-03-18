from datetime import datetime
#===================================================================
# Calculates Months with 1st day Sunday: needs Start and end of the year.
#===================================================================
start_year = 1901
end_year = 2000 #(calculates till Dec of this year)
Start_day_year = 0
start_day_mnth = 1

days_in_week = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
Sundays = 0
for yr in range(start_year,end_year+1):
    for mnth in range(1,13):
        if datetime(yr,mnth,1).weekday() == 6:
            Sundays+=1
        # print(f'{yr}:{mnth}:{days_in_week[datetime(yr,mnth,1).weekday()]}')
print(Sundays)            




#===================================================================
days_in_week = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
months_in_yr = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mnth_30 = [3, 5, 8, 10]
mnth_28 = [1]

lp_yr_flag = False
count = 0
for curr_yr in range(start_year,end_year+1):
    
    if curr_yr%4 ==0 and curr_yr%100 !=0 or curr_yr%400 ==0:
        lp_yr_flag = True
        #         Start_day_year = Start_day_year + 2    
    for curr_mnth in range(0,12):


        if start_day_mnth == 6 :
            count +=1
            # print(f'{curr_yr}:{months_in_yr[curr_mnth]}:{days_in_week[start_day_mnth]}')
        
        if start_day_mnth > 6:
            start_day_mnth = start_day_mnth - 7
        # print(f'{curr_yr}:{months_in_yr[curr_mnth]}:{days_in_week[start_day_mnth]}')
                
        if curr_mnth in mnth_30:
            start_day_mnth = start_day_mnth + 2
        elif curr_mnth in mnth_28:
            if lp_yr_flag:
                start_day_mnth = start_day_mnth + 1
        else:
            start_day_mnth = start_day_mnth + 3
    lp_yr_flag = False    

        
print(count)

# ----------------------------------------------
# September April June November =30 days
# Februry 29/30 days
# for curr_yr in range(1900,2001):
#     if Start_day_year > 6:
#         Start_day_year = Start_day_year - 7
 
#     print(f'{curr_yr}:{days_in_week[Start_day_year]}')
        
#     if curr_yr%4 ==0 and curr_yr%100 !=0 or curr_yr%400 ==0:
#         Start_day_year = Start_day_year + 2
#     else:
#         Start_day_year = Start_day_year + 1
    
#     if Start_day_year == 6:
#         count +=1
    
# print(count)

