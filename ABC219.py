# C
x=input()
n=int(input())
s=[input() for _ in range(n)]
y=[]
for i,alphabet in enumerate(x):
    y.append((i,alphabet))
ans=[]
scores=[]
for i in s:
    score=0
    for j in i:
        for k in y:
            if k[1] == j:
                score+=k[0]
    scores.append((score,i))
print(scores)    

# # B
# l=[]
# for _ in range(3):
#     l.append(input())
# t = input()
# ans=[]
# for i in t:
#     ans.append(l[int(i)-1])
# print(''.join(ans))


# #A
# x = int(input())
# if x >= 90 :
#     print('expert')
# elif 70 <= x < 90:
#     print(90 - x)
# elif 40 <= x < 70:
#     print(70 - x)
# else:
#     print(40 - x)
