n=int(input())
l=list(map(int, input().split()))

l.sort(reverse=True)
l.append(0)

count=0
pricount=0
tmp=l[0]

for i in l:
    # print('now',i)
    if i == tmp:
        count+=1
    else:
        print(count)
        pricount+=1
        count=1
        tmp=i

if pricount!=n:
    for _ in range(n-pricount):
        print(0)




# l2=list(set(l))
# l2.sort(reverse=True)

# if len(l2)<n:
#     for i in range(n-len(l2)):
#         l2.append(0)

# for j in l2:
#     if j!=0:
#         print(l.count(j))
#     else:
#         print(0)