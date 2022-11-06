from collections import Counter,defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(100000)

#C
n=int(input())
l=list(map(int, input().split()))

for i in range(n-1,0,-1):
    #リストを右から2つずつ比較 左がa
    a,b=l[i-1],l[i]
    #aのほうが大きい（昇順が崩壊した瞬間）
    if a>b:
        #cにaのインデックス番号を取得
        c=l.index(a)
        #cより左側のリストを一旦確保しておく
        left=l[:c]
        #基準となる大きなaを単独で確保しておく 単なる変数の付け替えにすぎないけども
        center=a
        #centerより右側の昇順になっている部分だけを確保
        right=l[c+1:]
        #確保したceterより最も小さい最も近い数はどれか
        for i in right[::-1]:
            if i<center:
                #該当のインデックス番号を取得
                tmp=right.index(i)
                #入れ替えを実施
                center,right[tmp]=i,center
                break
        #最終結合
        ans=left+[center]+right[::-1]
        print(*ans)

        # aa=l[:c]
        # ee=l[c:]
        # e=l[c+1:]
        # # print(aa,ee,e)
        # e.sort(reverse=True)
        # f=1000
        # for j in e:
        #     if b>j:
        #         f=j
        #         break
        # # print(aa,ee,f)
        # ff=ee.index(f)
        # ee[0],ee[ff]=f,ee[0]
        # # print(aa,ee,f)
        # gg=ee[ff-1:]
        # gg.sort(reverse=True)
        # ans=aa+[f]+gg
        # print(*ans)
        exit()



# l=[]
# for i in range(1,n+1):
#     l.append(str(i))
# l2=tuple(map(str, input().split()))
# A = list(itertools.permutations(l))
# B = A.index(l2)
# print(*A[B-1])





#A
# s=list(input())
# index=200
# for i,ss in enumerate(s):
#     if ss=='a':
#         index=i
# print(index+1 if index != 200 else '-1')

#B
# n,m =map(int, input().split())
# edge=[list() for _ in range(n+1)]

# for i in range(m):
#     a,b=map(int, input().split())
#     # a-=1
#     # b-=1
#     edge[a].append(b)
#     edge[b].append(a)
# edge.pop(0)
# # print(edge)

# for i in edge:
#     i.sort()
#     print(len(i),*i)

