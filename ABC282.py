from collections import Counter,defaultdict,deque
import itertools #product
import math
import sys

sys.setrecursionlimit(10**6)

'test'
#D


#C
n=int(input())
s=input()
cflg=0
ans=''
for i in s:
    if i == '"':
        cflg+=1
        ans+=i
        continue
    if i.islower():
        ans+=i
    else:
        if cflg%2==0:
            ans+='.'
        else:
            ans+=i
print(ans)


#B

# n,m=map(int, input().split())
# l=[list(input()) for _ in range(n)]
# ans=0
# for i in range(n):
#     for j in range(i+1,n):
#         for v,vv in zip(l[i],l[j]):
#             if v == 'x' and vv == 'x':
#                 break
#         else:
#             ans+=1
# print(ans)

#A

k=int(input())
ans=''
for i in range(k):
    a=chr(i+97)
    a=str.upper(a)
    ans+=a
print(ans)
