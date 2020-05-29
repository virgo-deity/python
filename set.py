a = set([1,2,3,4,5])
b = set([4,5,6,7,8])

print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.difference(b))
print(b.difference(a))
print(a.issuperset(b))
print(a.issubset(b))
 