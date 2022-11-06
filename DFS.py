#dfs
n,m=map(int, input().split())
l=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    l[a].append(b)


def dfs(v):
    if edge[v]:return
    edge[v]=True
    for vv in l[v]:
        dfs(vv)

ans=0

for j in range(n):
    edge=[False]*n
    dfs(j)
    ans+=sum(edge)
 
print(ans)



    # for v in range(j-1,-1,-1):
    #     if v in k:
    #         tmp+=1
    #         if tmp >= 2:
    #             continue
    # else:
    #     if tmp==1:
    #         ans+=1
    #         # print('vrange',j,k)


    # if j in k:
    #     a=k.index(j)
    #     b=k[:a]
    # if len(b)==1:
    #     ans+=1






# h=list(map(int, input().split()))
# l=[1]*n
# for i in range(m):
#     a,b=map(int, input().split())
#     if l[a-1]==1 and h[a-1] <= h[b-1]:
#         l[a-1]=0
#     if l[b-1]==1 and h[b-1]<=h[a-1]:
#         l[b-1]=0
# print(sum(l))
    


# n,m=map(int, input().split())
# l=[list() for _ in range(n)]
# for i in range(m):
#     a,b=map(int, input().split())
#     l[a-1].append(b-1)
#     l[b-1].append(a-1)
# for j in l:
#     print(len(j))