from itertools import product

#productを使った簡単なbit全探索の生成方法
#本来はビットシフトと&を使った2乗生成だが、productならラクラク生成

# 例: 数列Aから1つ以上いくつか選んだとき、その和が3で割り切れるものがあるかどうかを判定。
A = [1, 4, 13, 34]
n = len(A)
for bits in product([0, 1], repeat=n):
    print("bits: ", bits)
    a = [x for bit, x in zip(bits, A) if bit == 1] #ビットシフトしなくてもこれでOK 0のほうも使う場合は下にコピペして少し変えればOK
    if not a: continue #何も選ばれなかった場合はcontinue（ほぼ必須？）

    print("選んだもの: ", a)
    print("和: ", sum(a))
    if sum(a) % 3 == 0:
        print("Yes")
        exit()