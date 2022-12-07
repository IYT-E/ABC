from collections import Counter,defaultdict,deque
import itertools
import math
import sys

sys.setrecursionlimit(10**6)

#D
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
import collections
c = collections.Counter(prime_factorize(280))
maxi=0
for i,j in zip(c,c.values()):
    print(i,j)
    # maxi=max(i*j,max)
    # print(maxi)




#C
# s=list(input())
# s.append('0')
# t=list(input())
# cnt=1
# for i,j in zip(s,t):
#     if i != j:
#         print(cnt)
#         exit()
#     cnt+=1


#B
# n=int(input())
# l=list(map(int, input().split()))
# l.insert(0,0)
# l2=[]
# for i in range(1,n+1):
#     l2.append(l[i]-l[i-1])
# print(*l2)



# #A
# h,w=map(int, input().split())
# cnt=0
# for i in range(h):
#     cnt+=input().count('#')
# print(cnt)