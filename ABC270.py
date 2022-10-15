# #A
# a,b=map(int, input().split())
# #1,2,4 = 1,2,3(1,2),4,5(1,4),6(2,4),7(1,2,4)

# slist=[0]

# def sets(score):
#     if score == 1:
#         slist.append(1)
#     elif score == 2:
#         slist.append(2)
#     elif score == 3:
#         slist.append(1)
#         slist.append(2)
#     elif score == 4:
#         slist.append(4)
#     elif score == 5:
#         slist.append(1)
#         slist.append(4)
#     elif score == 6:
#         slist.append(2)
#         slist.append(4)
#     elif score == 7:
#         slist.append(1)
#         slist.append(2)
#         slist.append(4)
#     elif score == 0:
#         return

# sets(a)
# sets(b)

# slist=list(set(slist))

# print(sum(slist))


# B
# x,y,z=map(int, input().split())
# if x>y>z>0 or x<y<z<0:
#     print(abs(x-0))
# elif x>y>0>z or x<y<0<z:
#     print(abs(0-z)+abs(z-x))
# elif x>0>y or x<0<y or 0<x<y or 0>x>y:
#     print(abs(x-0))
# else:print(-1)


# C


