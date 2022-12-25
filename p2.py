from collections import deque

n=int(input())
l=list(map(int,input().split()))
hei=deque()
yasumi=deque()
cnt=0
ans=0
for i,v in enumerate(l):
    if v==1:
        hei.append(i)
    else:
        yasumi.append(i)

    if i<6:
        continue
    elif i==6:
        if len(yasumi)>=2:
            cnt=7
            ans=7

    else:
        if hei[0]<yasumi[0]:
            hei.popleft()
        else:
            yasumi.popleft()
        
        if len(yasumi)>=2:
            if cnt>=7:
                cnt+=1
                ans=max(ans,cnt)
            else:
                cnt=7
                ans=max(ans,cnt)
        else:
            cnt=0

print(ans)
