from collections import Counter,defaultdict,deque
import itertools #product
import math
import sys

sys.setrecursionlimit(10**6)

s=list(input())

ans=0

for i in itertools.product([0,1],repeat=len(s)):
    a = [x for bit, x in zip(i, s) if bit == 1]
    b = [x for bit, x in zip(i, s) if bit == 0]
    if a==[] or b==[]:
        continue
    a.sort(reverse=True)
    b.sort(reverse=True)
    a=''.join(a)
    b=''.join(b)
    ans=max(ans,int(a)*int(b))
print(ans)
    

