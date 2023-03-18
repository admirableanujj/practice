input = 100

a = 1
for i in range(1,input):
    a = a*i
ans = 0
for j in str(a):
    ans = ans + int(j)

print(ans)