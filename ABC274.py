# # A
# a,b=map(int, input().split())
# c=round(b/a,3)
# c=str(c)
# while len(c)<5:
#     c+='0'
# print(c)

# B
# h,w=map(int, input().split())
# l=[0]*w
# for i in range(h):
#     tmp=list(input())
#     for j,k in enumerate(tmp):
#         if k == '#':
#             l[j]+=1
# print(*l)

# C
n=int(input())
l=list(map(int, input().split()))
d={1:0}
print(0)
for i in range(n):
    am1=(i+1)*2 #8
    am2=(i+1)*2+1 #9
    now = l[i] #2
    d[am1]=d[now]+1
    d[am2]=d[now]+1
    print(d[now]+1)
    print(d[now]+1)
    # print(d)





