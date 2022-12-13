from collections import Counter,defaultdict,deque
import itertools #product
import math
import sys

sys.setrecursionlimit(10**6)


#D
Triple DP


#C
# n,t=map(int, input().split())
# a=list(map(int, input().split()))
# goukei=sum(a)
# amari=t%goukei
# for i,v in enumerate(a):
#     if v<amari:
#         amari-=v
#     else:
#         print(i+1,amari)
#         exit()

#B
# numbers10=['0','1','2','3','4','5','6','7','8','9']
# numbers9=['1','2','3','4','5','6','7','8','9']
# s=list(input())
# if len(s)<8:
#     print('No')
#     exit()
# for i,v in enumerate(s):
#     if i==0 or i==7:
#         if v.isupper():
#             pass
#         else:
#             print('No')
#             exit()
#     if i==1:
#         if v not in numbers9:
#             print('No')
#             exit()
#     if i==2 or i==3 or i==4 or i==5 or i==6:
#         if v not in numbers10:
#             print('No')
#             exit()
# print('Yes')

# #A
# n=int(input())
# for i in range(n,-1,-1):
#     print(i)