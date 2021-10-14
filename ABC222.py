#A
s=str(input())
print(s.zfill(4))

#B
n,p=map(int, input().split())
l=list(map(int, input().split()))
m=[i for i in l if i < p]
print(len(m))

#C
#ギブアップ
