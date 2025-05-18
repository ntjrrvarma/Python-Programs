n=100
s1=0
s2=0
d=0

for i in range(1,n+1):
    s1+=i
    s2=s2+int(pow(i,2))

d=pow(s1,2)-s2

print(d)
