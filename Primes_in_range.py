def is_prime(l):
    if l==1: return 0
    for j in range(2,int(l**(0.5))+1):
        if l%j==0:
            return 0
    return 1
n = int(input())
m = int(input())
k=0
for i in range(n,m+1):
    if is_prime(i): k+=1
print(k)