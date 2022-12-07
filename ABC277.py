from collections import Counter,defaultdict,deque
import itertools
import math
import sys

sys.setrecursionlimit(300000)

# C
n=int(input())
l=defaultdict(set)
for i in range(n):
    a,b=map(int, input().split())
    # a-=1
    # b-=1
    l[a].add(b)
    l[b].add(a)
if 1 not in l.keys():
    print('1')
    exit()

maxheight=1

# memo=[]
# memo.extend(l[1])
# memo.extend(l[4])
# print(memo)

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






# B
# n=int(input())
# l=[input() for _ in range(n)]
# l2=set(l)
# if len(l)!=len(l2):
#     print('No')
#     exit()
# c1=['H','D','C','S']
# c2=['A','2','3','4','5','6','7','8','9','T','J','Q','K']
# cards=[]
# for i in c1:
#     for j in c2:
#         cards.append(i+j)
# for k in l2:
#     if k not in cards:
#         print('No')
#         exit()
# else:print('Yes')
    
# A
# n,x=map(int, input().split())
# l=list(map(int, input().split()))
# print(l.index(x)+1)