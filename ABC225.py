#A
# s=set(input())
# if len(s) == 3:
#     print(6)
# elif len(s) == 2:
#     print(3)
# else:
#     print(1)

#B
n=int(input())
tmp=[]
tmp2=[]
for _ in range(n-1):
    a,b=map(int, input().split())
    tmp.append(a)
    tmp2.append(b)
if len(set(tmp)) + 1 == n or len(set(tmp2)) + 1 == n:
    print('Yes')
else:
    print('No')
