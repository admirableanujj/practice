# Number Spiral Diagonal
# In this question I have to design a spiral move right in the clockwise direction.Since the direction is specified the problem becomes simple.
n = 1001
a = []

for i in range(1, n*n+1):
    a.append(i)

nearest_diagonal = 2    
j=2
a_sum = 1
sum_arr = {0:[1]}
times = 0
foo = []
while j < len(a):
    times +=1
    foo.append(a[j])
    sum_arr.update({nearest_diagonal:foo})
    a_sum = a_sum + a[j]
    if times>=4:
        times = 0
        foo = []
        nearest_diagonal = nearest_diagonal+2
    j = j+nearest_diagonal
 
print(f'a_sum:{a_sum}')
print(f'sum_arr:{sum_arr}')
        
    
    