#ARC125
N,M=map(int, input().split())
S=list(map(int, input().split()))
T=list(map(int, input().split()))
saitan = 10**6
S2=[0,0]
cnt=0
tmp=0
if S[0] != S[-1]:
    for i in T:
        if i == S[-1]:
            cnt+=2
            tmp = S[0]
            S[0] = S[1]
            S[1] = tmp
        else:
            cnt+=1
    print(cnt)
    exit()

for i in range(N-1):
    if S[0+i]!=S[1+i]:
        saitan=i
        S2[0]=S[0+i]
        S2[1]=S[1+i]
        if N-saitan < saitan:
            saitan = N-saitan
            S2[0]=S[saitan]
            S2[1]=S[saitan-1]

if saitan == 10**6:
    T=list(set(T))
    if len(T) == 1 and S[0] == T[0]:
        print(M)
    else:
        print(-1)
        exit()

for i in T:
    if i == S2[0]:
        cnt+=1
    else:
        cnt+=2
        tmp = S2[0]
        S2[0] = S2[1]
        S2[1] = tmp        

print(cnt+saitan)