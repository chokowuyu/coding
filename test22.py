a, b = set(map(int,input().split()))
a = {i for i in range(1,a+1) if a % i == 0}
b = {j for j in range(1,b+1) if b % j ==0}
divisor = a & b
 
result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)