# #A
# n=int(input())
# l=list(map(int, input().split()))
# maxtall=0
# ans=0
# for i,tall in enumerate(l):
#     if maxtall<tall:
#         maxtall=tall
#         ans=i+1
# print(ans)
    
# #B
# l=list(map(int, input().split()))
# print(((l[0]*l[1]*l[2])-(l[3]*l[4]*l[5]))%998244353)

#C
import itertools
l=[list(input()) for _ in range(9)]
p=[]
for i,col in enumerate(l):
    for j,row in enumerate(col):
        if row=='#':
            p.append([i,j])
#重複なしで異なる2点を選んで格納
sq = itertools.combinations(p, 2)

cnt=0

for j in sq:
    #右直線もしくは右下方向の2点が決まる
    if j[0][0] <= j[1][0] and j[1][1] - j[0][1] > 0:
        x=abs(j[0][0]-j[1][0])
        y=abs(j[0][1]-j[1][1])
        #この絶対値を逸脱する場合は絶対に正方形は8ｘ8の範囲内では作れない
        if x>7 or y<1 or y>8:
            continue
        #第3点が求まる
        p3r=j[1][0]+y
        p3c=j[1][1]-x
        #第3点が範囲外にあったら駄目
        if p3r>8 or p3c<0:
            continue
        p3=[p3r,p3c]
        #第3点が#かどうか
        if p3 not in p:
            continue
        #第4点が求まる、以降第3点と同じ判定
        p4c=p3[1]-y
        p4r=p3[0]-x
        if p4c<0 or p4r<0:
            continue
        p4=[p4r,p4c]
        if p4 not in p:
            continue
        #全通過で正方形判定
        cnt+=1
    else:
        continue
#かぶりははじめから除外済み
print(cnt)
