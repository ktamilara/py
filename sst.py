s,t=input().split()
s=int(s)
t=int(t)
y=0
count=0
c= list(map(int, input().split()))
for a in c:
    if a==t:
        count=count+1
if count!=0:
    print('yes')
else:print('no')
