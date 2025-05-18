a=1
b=2
c=0
s=0
n=4000000   
l=[]
l.append(a)
l.append(b)
while b<n:
    l.append(a+b)
    c=b
    b=b+a
    a=c

for i in l:
    if i%2==0:
        s+=i

print(s)
    
