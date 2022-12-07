from collections import Counter,defaultdict,deque
import itertools
import math
import sys

sys.setrecursionlimit(10**6)

#D
a,b=map(int, input().split())
superman=10**18
cnt=0
g=1
while True:
    c=(b*cnt)+(a/math.sqrt(g))
    superman=min(c,superman)
    if c>superman:
        print(superman)
        exit()
    cnt+=1
    g+=1


# C
# h,w=map(int, input().split())
# d1=['']*w
# d2=['']*w
# for i in range(h):
#     s=input()
#     for j,v in enumerate(s):
#         d1[j]+=v
# d1.sort()
# for i in range(h):
#     s=input()
#     for j,v in enumerate(s):
#         d2[j]+=v
# d2.sort()
# print('Yes' if d1==d2 else 'No')

# h,w=map(int, input().split())
# d1=[]
# d2=[]
# for i in range(h):
#     s=list(input())
#     d1.append(s)
    
# for i in range(h):
#     s=list(input())
#     d2.append(s)

# for i,j in zip(d1,d2):
#     i.sort()
#     j.sort()
#     if i!=j:
#         print('No')
#         exit()

# print('Yes')




# s1=set()
# for i in d1.values():
#     s1.add(i)
# s2=set()
# for i in d2.values():
#     s2.add(i)
# print('No' if bool(s1-s2) else 'Yes')




# B
# s=input()
# t=input()
# print('Yes' if t in s else 'No')


# A
# s=input()
# a=s.count('v')
# b=s.count('w')
# print(a+(b*2))
