# #B
# s=input()
# t=input()

# if len(s)>len(t):
#     print('No')
#     exit()

# print('Yes' if s==t[:len(s)] else 'No')


#C
N = int(input())
p_list = list(map(int, input().split()))
#C問題でよくある一時リスト 回転番号の記録用
count_list = [0] * N
#各料理についてのループを行う
for i in range(N):
    # i番目の料理を喜ぶ人の回転番号（各人3つ）が一時リストに記録され回転番号のインデックスごとに蓄積していく
    count_list[(p_list[i]-i-1)%N] += 1
    count_list[(p_list[i]-i)%N] += 1
    count_list[(p_list[i]-i+1)%N] += 1
print(count_list)
print(max(count_list))
#人の順番（整頓済み）、料理の並び順（ランダム）、回転番号一時リスト という3つを意識することがカギだった