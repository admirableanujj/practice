import csv
import string

alphabets = string.ascii_uppercase
print(alphabets.index('C'))
f = open(r'p022_names.txt')
lines = f.read().split(',')
lines.sort()
ans = 0
x = '"COLIN"' 
for line in lines:
    # line = line.replace('"','')
    fact_1 = 0
    for letter in line.replace('"',''):
        fact_1 += alphabets.index(letter)+1
    fact_2 = lines.index(line)+1
    
    ans+=fact_1*fact_2
    
print(ans)
ans2 = 0
for line in lines:
    if line == x:
        # line = line.replace('"','')
        fact_1 = 0
        for letter in line.replace('"',''):
            fact_1 += alphabets.index(letter)+1
        fact_2 = lines.index(line)+1
        print(f'x:{fact_1}||y:{fact_2}')
        ans2+=fact_1*fact_2        

print(ans2)        


# print(lines)

# print(type("CLAY"))
