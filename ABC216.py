N=int(input())
ans = ""
for _ in range(120):
    if N % 2 == 0:
        N = N // 2
        ans = 'B' + ans
        if N == 0:
            break
    else:
        N = N - 1
        ans = "A" + ans
        if N == 0:
            break
print(ans)