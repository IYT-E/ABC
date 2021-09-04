#C
n=int(input())
p=list(map(int, input().split()))
q = [0]*n
for i in range(1,n+1):
    q[p[i-1]-1] = i
print(' '.join(map(str,q)))

#B
atcoder = ["ABC" , "ARC" , "AGC" , "AHC"]
for _ in range(3):
    s = input()
    if s in atcoder:
        atcoder.remove(s)
print(atcoder[0])

#A
t=input().split()
s=sorted(t)
print("Yes" if t == s else "No")