from maths import quick_math as m


upper_limit = 10**5
number = 10
required_sum = 0
while True:
    
        number += 1
        digit_arr = []
        for i in range(0,len(str(number))):
            digit = number/10**i % 10
            digit_arr.append(int(digit))
        factorial_sum = 0
        for digit in digit_arr:
            factorial_sum += m.factorial(digit)
        if factorial_sum == number:
            print(f"Found: {number}:{digit_arr}")
            required_sum += number
            print(f"Sum of all numbers: {required_sum}")
        if factorial_sum/number > upper_limit:
             break
            
print(f"Sum of all numbers: {required_sum}")

        
        


    
