# def rec(num):
#     if num == 0:
#         return 1
#     else:
#         return num * rec(num-1)
# print(rec(int(input())))


# x,k=map(int, input().split())

# for i in range(k):
#     x=str(x)
#     y=list(x)
#     if y[-i-1]=='5':
#         y[-i-1]='6'
#         # print('if',y)
#     x=''.join(y)
#     x=int(x)
#     x=round(x,-i-1)
#     if x==0:
#         print(0)
#         exit()
#     # print(x)

# print(x)

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



