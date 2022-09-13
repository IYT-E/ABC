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
n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
#print(n,m,a)

#初期値はマイナスの最小値
ans=-10**16

#累積和 nのリスト全部分
rw=[0]
for i in range(n):
  rw.append(rw[i]+a[i])
# print(rw)

#左端のmをまず求めてnowに格納する 
now=0
for i in range(m):
  now+=(i+1)*a[i]
# print(now)

#左端ぶんのans判定
ans=max(ans,now)

# n-mは左端ぶんから引いた残りの数 その分だけforを回す
for i in range(n-m):
    # 内部変数nxtを定義 左端累計のnowから (累積和rwのnow外右から左を引いた数)＋(右のインデックス数(常にmになる）＊リスト内該当数字) を引く
    # やってることは想像通りだが累積和の法則を活かした形が違った
  nxt=now-(rw[i+m]-rw[i])+m*a[i+m]
    #nwxをnowに置き換えてmax判定 考え方は予想通り
  now=nxt
  ans=max(ans,now)
# print(ans)