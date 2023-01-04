#A023
from collections import deque
N=int(input())
l=list(map(int,input().split()))
heijitsu=deque()
holiday=deque()
count=0
ans=0
for i,v in enumerate(l):
    if v==1:
        heijitsu.append(i)
    else:
        holiday.append(i)
    if i<6:
        continue
    elif i==6:
        if len(holiday)>=2:
            count=7
            ans=7
    else:
        if len(holiday)>0 and len(heijitsu)>0:
            if heijitsu[0]<holiday[0]:
                heijitsu.popleft()
            else:
                holiday.popleft()
        elif len(holiday)==0:
            heijitsu.popleft()
        else:
            holiday.popleft()
        if len(holiday)>=2:
            if count>=7:
                count+=1
                ans=max(ans,count)
            else:
                count=7
                ans=max(ans,count)
        else:
            count=0
print(ans)
