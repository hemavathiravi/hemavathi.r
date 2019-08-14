#h
    
r=input()
l1=len(r)
count=0
for i in range(0,l1):
    if(r[i]=="("):
        count=count+1
    elif(r[i]==")"):
        count=count-1
if(count==0):
    print("yes")
else:
    print("no")
