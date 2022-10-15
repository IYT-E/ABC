# # A
# i=int(input())
# print(hex(i)[2:].upper().zfill(2))

# B
# n,q=map(int, input().split())
# l=[list(map(int, input().split())) for _ in range(n)]
# q=[list(map(int, input().split())) for _ in range(q)]

# for i in q:
#     print(l[i[0]-1][i[1]])

# C
n=int(input())
l=list(map(int, input().split()))

#1冊だけ1巻じゃないのを持っている場合の処理
if n==1:
    if l[0] != 1:
        print(0)
        exit()

#ダブリはなくしちゃおうね
l2=list(set(l))
#ダブりは何冊？
mod=len(l)-len(l2)
#2で割って新規購入可能な数を出す
buyable_books=mod//2
#半端の余りを出す
tmp=mod%2
#読めた巻数の初期セット
cnt=0
#売っちゃった巻数をカウント
sold=0
#売って見た場合のためのカウント
anaume=1

for i,j in enumerate(l2):
    #今見たい巻数
    desire=i+anaume
    print('now desire is',desire)
    print('now j is',j)
    #jは今見たい巻数か
    if j == desire:
        cnt+=1
        print('just desire',cnt)
    else:
        #購入可能ならば
        if buyable_books:
            buyable_books-=1
            cnt+=1
            print('buy stock',cnt)
        else:
            #半端があれば1冊だけ売る
            if tmp:
                #最後尾が今参照している巻数ならばそれを売って終わり
                if l2[-i-1] == j:
                    cnt+=1
                    print(cnt)
                    exit()
                #最後尾が今参照している巻数でないならばそれを売って売ったリストに入れてcnt増やしてとりあえず終わり
                #tmpがある場合は1回しかありえないのでとりあえず
                elif l2[-i-1] != j:
                    cnt+=1
                    sold-=1
            #半端がなければ最大2冊売らなければいけない
            else:
                #最後尾もしくは最後尾から2番めが今参照している巻数ならばもう売れず穴埋めはできないのでcntを表示して終わり
                if l2[-i-1] == j or [-i-2] == j:
                    print('cannot sold',cnt)
                    print(cnt)
                    exit()
                else:
                    #すでに売っていても終わり
                    if l2[sold-1] == j or l2[sold-2] == j:
                        print('already sold',cnt)
                        print(cnt)
                        exit()
                    #売る処理
                    else:
                        cnt+=1
                        sold-=2
                        print('solded1',sold)
                        while j > desire+anaume:
                            sold-=2
                            if l2[sold-1] == j or l2[sold-2] == j:
                                print('while sold',cnt,sold)
                                print(cnt)
                                exit()
                            cnt+=1
                            anaume+=1
                        

if buyable_books:
    cnt+=buyable_books
print(cnt)


