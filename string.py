s=list(map(str,input()))
q=0
t=0
for k in range(0,len(s)):
    if p[k].isdigit()==True:
        q=q+1
    elif s[k].isalpha()==True:
        t=t+1
if t>0 and q>0:
    print("Yes")
else: print("No")
