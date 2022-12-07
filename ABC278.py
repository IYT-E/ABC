# D
from collections import Counter,defaultdict
n=int(input())
d=defaultdict(int)
a=list(map(int, input().split()))
q=int(input())
for i,v in enumerate(a):
    d[i]=v
for i in range(q):
    qu=list(map(int, input().split()))
    if qu[0]==3:
        print(d[qu[1]-1])
    if qu[0]==2:
        d[qu[1]-1]+=qu[2]
    if qu[0]==1:
        d=defaultdict(int)




# # C
# from collections import Counter,defaultdict
# n,q=map(int, input().split())
# l=defaultdict(int)
# for i in range(q):
#     t,a,b=map(int, input().split())
#     # a-=1
#     # b-=1
#     s=str(a)+'-'+str(b)
#     if t==1:
#         l[s]=True
#     if t==2:
#         l[s]=False
#     if t==3:
#         s2=str(b)+'-'+str(a)
#         print('Yes' if l[s] == True and l[s2]==True else 'No')
#     # print(l)








# #B
# h,m=map(str, input().split())
# h=h.zfill(2)
# m=m.zfill(2)

# a,b,c,d=int(h[0]),int(h[1]),int(m[0]),int(m[1])

# def hantei(a,b,c,d):
#     if a<2 and b<6 and c<10:
#         a,b,c,d=str(a),str(b),str(c),str(d)
#         print(a+b,c+d)
#         exit()
#     elif a==2 and b<6 and c<4:
#         a,b,c,d=str(a),str(b),str(c),str(d)
#         print(a+b,c+d)
#         exit()

# while True:
#     # print(a,b,c,d)
#     hantei(a,b,c,d)
#     d+=1
#     if d==10:
#         d=0
#         c+=1
#         if c==6:
#             c=0
#             b+=1
#             if a==0:
#                 if b==10:
#                     a=1
#                     b=0
#             elif a==1:
#                 if b==10:
#                     a=2
#                     b=0
#             elif a==2:
#                 if b==5:
#                     a,b=0,0
#     if a==2 and b==4 and c==0 and d==0:
#         a,b,c,d=0,0,0,0

    # hh=str(a)+str(b)
    # mm=str(c)+str(d)
    # hh=int(hh)
    # mm=int(mm)
    # mm+=1
    # if mm==0


#A
# n,k=map(int, input().split())
# a=list(map(int, input().split()))
# for i in range(k):
#     a.pop(0)
#     a.append(0)
# print(*a)