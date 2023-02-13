
import number2words

ones = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    0:''
}

tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty', 'ninety', 'hundred']
hundreds = ['hundred']
total_sum = 0

for i in range(1,1000+1):
    input = i

    if input < 20:
        ans = ones[input]
    else:
        if input <100:
            x10 = tens[input//10]
            input = input - input//10*10
            x1 = ones[input]
            ans = x10+x1

        else:
            if input <1000:
                x100 = ones[input//100] + ' hundred '
                input = input - input//100*100
                
                if input < 20:
                    if input == 0 :
                        x1 = '' 
                    else:
                        x1 = ' and ' + ones[input]
                    ans = x100+x1
                else:
                    x10 = tens[input//10]
                    input = input - input//10*10
                    x1 = ones[input] 
                    ans = x100+ ' and '+x10+x1
            elif input == 1000:
                ans = 'one thousand'
    total_sum = total_sum + len(ans.replace(' ',''))


print("TakeIt:",total_sum)

