l=['O','I','Z','E','A','S','G']
s=input()
ss=''
for i in s:
    if i in l:
        ss+=str(l.index(i))
    else:
        ss+=i
print(ss)
