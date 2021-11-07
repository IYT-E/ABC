# Aでこんなのやらすな！
from decimal import *
v = float(input())
c = Decimal(str(v)).quantize( Decimal('0') , rounding=ROUND_HALF_UP )
print(c)

#BでCみたいな計算量削減の問題出すな！！！
n=int(input())
li = []
xli=[]
cnt=0
for i in range(n):
    l = list(map(int, input().split()))
    l.pop(0)
    if l in xli:
        continue
    if l in li:
        xli.append(l)
    else:
        li.append(l)
        cnt+=1
print(cnt)

