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




# ABC277 C 無向閉路ありのDFSで最長経路探索
from collections import defaultdict
n=int(input())
l=defaultdict(set)
for i in range(n):
    a,b=map(int, input().split())
    l[a].add(b)
    l[b].add(a)
if 1 not in l.keys():
    print('1')
    exit()

maxheight=1
memo=set()

def dfs(n):
    global maxheight
    global memo
    tmp=max(l[n])
    maxheight=max(maxheight,tmp)
    for vv in l[n]:
        if vv in memo:
            continue
        memo.add(vv)
        dfs(vv)

dfs(1)
print(maxheight)

# 同上のdequeを使ったwhile作戦
que = deque()
que.append(1)
S = {1}
while que:
	v = que.popleft()
	for i in graph[v]:
		if not i in S:
			que.append(i)
			S.add(i)
print(max(S))




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