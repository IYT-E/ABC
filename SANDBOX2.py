n = int(input())
p = list(map(int, input().split()))

#jにリスト長から2を引いた数を置く
j = n - 2

# 9 8 6 5 10 3 1 2 4 7
#右から2個ずつ比べてる？ あってる。右の昇順を確認してる
# j=8 | j+1=9
while p[j] < p[j + 1]:
  j -= 1
#昇順が崩れる位置のjのみを記録している

# kはリストの最終位置にとりあえず置く
k = n - 1
# 右から見ていく処理のwhile版かこれ でkは昇順が崩れた数字より最も近く小さい数字のインデックスがわかるというわけだ
while p[j] < p[k]:
  k -= 1

# 入れ替え処理
p[j], p[k] = p[k], p[j]

# 9 8 6 5 10 2 1 3 4 7
# 昇順が崩れる位置（入れ替え済み）を含む左側＋含まない右側逆順
print(j)
print(*p[:j + 1], *p[:j:-1])
