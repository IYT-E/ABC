#A
# s=input()
# l=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# print(5-l.index(s))

# #B
# s=input()
# if s[0]=='1':
#     print('No')
#     exit()

# l=[0]*7

# if s[6]=='1':
#     l[0]=1
# elif s[6]=='0':
#     l[0]=0

# if s[3]=='1':
#     l[1]=1
# elif s[3]=='0':
#     l[1]=0

# if s[7]=='1' or s[1]=='1':
#     l[2]=1
# elif s[7]=='0' and s[1]=='0':
#     l[2]=0

# if s[4]=='1':
#     l[3]=1
# elif s[4]=='0':
#     l[3]=0

# if s[2]=='1' or s[8]=='1':
#     l[4]=1
# elif s[2]=='0' and s[8]=='0':
#     l[4]=0

# if s[5]=='1':
#     l[5]=1
# elif s[5]=='0':
#     l[5]=0

# if s[9]=='1':
#     l[6]=1
# elif s[9]=='0':
#     l[6]=0

# l2=''.join(map(str,l))

# ju=['101','1001','10001','100001','1000001']

# for i in ju:
#     if i in l2:
#         print('Yes')
#         exit()
# else:print('No')

#C
n,m=map(int, input().split())
l=list(map(int, input().split()))

indexsum=sum(l[0:m])
tmp=0
for i in range(m):
    tmp+=(i+1)*l[i]
    print(tmp)

if n==m:
    print(tmp)
    exit()

max=tmp

for j in range(1,n-m+1):
    indexsum=indexsum-l[j-1]
    tmp=tmp-indexsum+(m)*l[j+m-1]
    indexsum+=l[j+m-1]
    print('for',tmp)
    if tmp>max:
        max=tmp

print(max)

