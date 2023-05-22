import math
a,b,c=map(int,input().split())
s = (a+b+c)*0.5
y = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("%.2f"%y)