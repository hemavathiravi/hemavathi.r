#h
r,h,v=map(str,input().split())
r=list(r)
h=list(h)
v=int(v)
count=0
for i in range(0,len(r)):
        if(n[i]!=k[i]):
            count=count+1
if(count==v):
    print("yes")
else:
    print("no")
