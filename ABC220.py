#A
a,b,c=map(int, input().split())
for i in range(a,b+1):
    if i % c == 0:
        print(i)
        exit()
print('-1')

#B
k=int(input())
a,b=map(int, input().split())
print(int(str(a),k)*int(str(b),k))

#C
n=int(input())
lista=list(map(int, input().split()))
x=int(input())
sumlist=sum(lista)
if x < sumlist:
    cnt = 0
    sumsum = 0
    for i in lista:
        sumsum += i
        cnt +=1
        if x < sumsum:
            print(cnt)
            exit()
j = x // sumlist
cnt = j * len(lista)
sumsum = sumlist * j
for i in lista:
    sumsum += i
    cnt +=1
    if x < sumsum:
        print(cnt)
        exit()