# #A
# a,b=map(int, input().split())
# print(32 ** (a-b))

#B　俺のプログラムがこんなに汚いわけがない（でも通過）
# s=input()
# t=input()
# score=0
# for i,j in zip(s,t):
#     if i!=j:
#         score +=1

# k=[]
# l=[]
# flag=0

# if score == 0:
#     print('Yes')
# elif score ==1:
#     print('No')
# elif score >2:
#     print('No')
# elif score == 2:
#     for i,j in zip(s,t):
#         if flag==1:
#             if i==j:
#                 print('No')
#                 exit()
#         if i!=j:
#             k.append(i)
#             l.append(j)
#             flag+=1
#     if k[0]==l[1] and k[1]==l[0]:
#         print('Yes')        
#     else:
#         print('No')

#C うんこプログラム
import itertools
import copy

n=input()
maxim=0

if len(n)==3:
    a=int(n[0])*int(n[1]+n[2])
    b=int(n[0])*int(n[2]+n[1])
    c=int(n[1])*int(n[0]+n[2])
    d=int(n[1])*int(n[2]+n[0])
    e=int(n[2])*int(n[1]+n[0])
    f=int(n[2])*int(n[0]+n[1])
    
    print(max(a,b,c,d,e,f))
    exit()
    
n=sorted(n,reverse=True)
a,b=[],[]
a.append(n[0])
b.append(n[1])
n.pop(0)
n.pop(0)
l=list(itertools.permutations(n))

for i in l:
    c=copy.copy(a)
    d=copy.copy(b)
    for j,num in enumerate(i):
        if  j%2 == 0:
            c.append(num)
        else:
            d.append(num)
    c=int(''.join(c))
    d=int(''.join(d))
    if maxim < c*d:
        maxim = c*d
print(maxim)

