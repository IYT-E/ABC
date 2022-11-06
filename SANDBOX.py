from collections import Counter,defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(100000)

n,x=map(int, input().split())
x-=1
l=list(map(int, input().split()))
l=list(map(lambda x:x-1,l))
ln=[False]*n
ln[x]=True
tmp=l[x]
while True:
    if ln[tmp]==True:
        print(sum(ln))
        exit()
    else:
        ln[tmp]=True
        tmp=l[tmp]
