# シンプルDP（与えられたカードの合計数、指定数以下の最大値は）
def find_max_dp(num_list, limit): #リスト、指定数
    list_len = len(num_list)
    #2次元配列の生成、縦方向にカードの数、横方向に指定数 指定数は10だとすると0スタートなので＋1の11箇所必要
    dp_table = [[0 for j in range(limit + 1)] for i in range(list_len)] 
 
    # 1番目のカード
    for j in range(limit + 1):
        # 1番目のカードを追加 縦0の横方向の指定数リストを0から見ていって該当の数字以上はすべてその数字で埋める
        if num_list[0] <= j:
            dp_table[0][j] = list[0] 
 
    # 2番目以降のカード
    #縦方向
    for i in range(list_len):
        #横方向
        for j in range(limit + 1):
            # ひとつ前のカードを参照 1枚めはリストの−1なので最後のカードを参照するが全部0なので問題ない tmpは0になる
            tmp_not_choice = dp_table[i-1][j]
            if num_list[i] > j: # コスト不足のとき 1枚めは普通に同じ数で更新するだけ
                dp_table[i][j] = tmp_not_choice 
            else:
                tmp_choice = dp_table[i-1][j - num_list[i]] + num_list[i]
                dp_table[i][j] = max(tmp_choice,tmp_not_choice)
 
    return dp_table[list_len - 1][limit]
 
list = [4,2,9,7,5,6] #実際に与えるリスト
print(find_max_dp(list,21))



# ナップサックDP
# 入力の受け取り
N,W=map(int, input().split())

# (1)表を作る
dp=[[0]*(W+1) for i in range(N+1)]

# (3)表の小さい方から答えにたどり着くまで埋める
# i=1~N
for i in range(1,N+1):
    # i番目の品物の重さ,価値
    wi,vi=map(int, input().split())

    # w=0~W
    for w in range(W+1):
        # w-wiがマイナスなら
        if w-wi<0:
            # i番目の品物を入れない
            dp[i][w]=dp[i-1][w]
        # 0≤w-wiなら
        else:
            # i番目の品物を入れない
            # i番目の品物を入れる
            # どちらか大きい方
            dp[i][w]=max(dp[i-1][w],dp[i-1][w-wi]+vi)

# (4)答えを出力する
print(dp[N][W])



# ジャンプ系DP
def solve():
    N, X = map(int, input().split())
    dp = [[False] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        a, b = map(int, input().split())
        for j in range(X + 1):
            if dp[i][j]:
                if j + a <= X:
                    dp[i + 1][j + a] = True
                if j + b <= X:
                    dp[i + 1][j + b] = True
    return dp[N][X]


print("Yes" if solve() else "No")