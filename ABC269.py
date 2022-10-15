# # A
# a,b,c,d=map(int, input().split())
# print((a+b)*(c-d))
# print('Takahashi')

# B
# li=[input() for _ in range(10)]
# a,b,c,d=0,0,0,0
# hcnt=0
# tmp=[]

# for i,j in enumerate(li):
#     if '#' in j:
#         b=i+1
#         hcnt+=1
#         tmp=j

# a=b-hcnt+1

# wcnt=0
# for i,j in enumerate(tmp):
#     if j=='#':
#         d=i+1
#         wcnt+=1

# c=d-wcnt+1

# print(a,b)
# print(c,d)


# C
import itertools
n=int(input())
print('0')
binn=bin(n)[2:]
# print(type(binn)) str 1011

binn=list(binn)
binn.reverse()

onenum=[]
for i,j in enumerate(binn):
    if j=='1':
        onenum.append(i)

# print(onenum)

list2=[]

for i in range(1,len(onenum)+1):
    all = itertools.combinations(onenum,i)
    for j in all:
        nulu=['0']*61
        for k in j:
            nulu[-k-1]='1'
        list2.append(int(''.join(nulu),2))
            # nulu[int(k)+1]='1'
            # print(int(nulu,2))

list3=[]

for i in list2:
    list3.append(int(i))

list3.sort()

for i in list3:
    print(i)



# print(int('100000000000000000001000000000000000000010000000000000000000',2))