import collections

n=int(input())
l=list(map(int, input().split()))

l.sort()

print(collections.Counter(l))