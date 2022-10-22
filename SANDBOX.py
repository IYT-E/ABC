n,m=map(int, input().split())
l=[list(map(int, input().split())) for i in range(m)]
# [[1, 7], [3, 2], [1, 7]]
d={i:0 for i in range(1,n+1)}
# {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for j in l:
    if d[j[0]]==0:
        d[j[0]]=j[1]
        continue
    elif d[j[0]]!=j[1]:
        print(-1)
        exit()
ans=''
for k in d.values():
    ans+=str(k)
if ans[0]=='0':
    print('-1')
    exit()
print(ans)