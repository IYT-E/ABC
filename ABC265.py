#A
# x,y,n=map(int, input().split())
# tmp1=0
# tmp2=0
# if n>=3:
#     tmp1=(n//3*y)+(n%3*x)
#     tmp2=n*x
#     print(tmp1 if tmp1 < tmp2 else tmp2)
# else:
#     print(n*x)

#B
# n,m,t=map(int, input().split())
# a=list(map(int, input().split()))

# b=[0 for _ in range(n)]
# for i in range(m):
#     tmp = list(map(int, input().split()))
#     b[tmp[0]-1]=tmp[1]

# for i in range(1,n+1):
#     #ゴール判定
#     if i==n:
#         print('Yes')
#         exit()
#     #ボーナスタイム加算処理
#     t+=b[i-1]
#     #移動に伴うタイム減算処理
#     t-=a[i-1]
#     #タイム切れ判定
#     if t<=0:
#         print('No')
#         exit()
# else:print('Yes')

#C
h,w=map(int, input().split())
grid=[list((input())) for _ in range(h)]

nowh=0
noww=0

for i in range(300000):
    s=grid[nowh][noww]
    if s=='U':
        if nowh==0:
            print(nowh+1,noww+1)
            exit()
        nowh-=1
    elif s=='D':
        if nowh==h-1:
            print(nowh+1,noww+1)
            exit()
        nowh+=1
    elif s=='R':
        if noww==w-1:
            print(nowh+1,noww+1)
            exit()
        noww+=1
    elif s=='L':
        if noww==0:
            print(nowh+1,noww+1)
            exit()
        noww-=1
else:print("-1")
