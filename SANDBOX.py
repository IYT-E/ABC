s=input()
t=input()
l1=list(s)
l2=list(t)
l1.sort()
l2.sort(reverse=True)
''.join(l1)
''.join(l2)
if l1==l2:
    print('No')
elif l1<l2:
    print('Yes')
else:print('No')